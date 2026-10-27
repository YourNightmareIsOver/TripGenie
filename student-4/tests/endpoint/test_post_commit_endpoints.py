"""Post-commit endpoint tests against the live Student 4 Compose stack.

student-4-ci.yml's compose job runs these over HTTP once the slice and the
shared reference service are up, so they exercise the built images rather than
in-process apps. The two endpoint functions under test are creating and reading
an activity, and searching activities with QUERY /activity. Without
STUDENT4_ENDPOINT_BASE_URL the module is skipped, so ordinary pytest runs stay
offline.
"""

from __future__ import annotations

import os
import uuid
from typing import TYPE_CHECKING, Any

import httpx
import pytest

if TYPE_CHECKING:
    from collections.abc import Iterator

BASE_URL = os.environ.get("STUDENT4_ENDPOINT_BASE_URL", "")

pytestmark = pytest.mark.skipif(
    not BASE_URL, reason="STUDENT4_ENDPOINT_BASE_URL is not set"
)


@pytest.fixture(scope="module")
def client() -> Iterator[httpx.Client]:
    with httpx.Client(base_url=BASE_URL, timeout=10) as http:
        http.get("/ready").raise_for_status()
        yield http


def activity_payload(name: str, **overrides: object) -> dict[str, Any]:
    return {
        "name": name,
        "description": "Post-commit CI paddle on the harbour.",
        "price": "89.50",
        "pricing_basis": "PER_PERSON",
        "duration_minutes": 120,
        "minimum_participants": 1,
        "maximum_participants": 8,
        "booking_required": True,
        "is_active": True,
        "location_details": {"country": "Australia", "city": "Sydney"},
        "categories": ["ADVENTURE"],
        "availability_schedules": [
            {
                "recurring_weekly": True,
                "day_of_week": "MONDAY",
                "start_time": "09:00",
                "end_time": "12:00",
            }
        ],
    } | overrides


@pytest.fixture
def activity(client: httpx.Client) -> Iterator[dict[str, Any]]:
    name = f"CI kayak {uuid.uuid4().hex[:10]}"
    response = client.post("/activity", json=activity_payload(name))
    assert response.status_code == 201, response.text
    created: dict[str, Any] = response.json()
    yield created
    # Remove it again so reruns against the same stack start clean.
    client.delete(f"/activity/{created['id']}")


# ---------------------------------- endpoint 1: create and read an activity


def test_a_created_activity_is_stored_and_read_back(
    client: httpx.Client,
    activity: dict[str, Any],
) -> None:
    response = client.get(f"/activity/{activity['id']}")

    assert response.status_code == 200, response.text
    stored = response.json()
    assert stored == activity
    assert stored["price"] == "89.50"
    assert stored["pricing_basis"] == "PER_PERSON"
    assert stored["categories"] == ["ADVENTURE"]
    # Names are resolved back through the shared reference service.
    assert stored["location_details"]["country"].lower() == "australia"
    assert stored["location_details"]["city"].lower() == "sydney"


def test_an_activity_with_an_unknown_category_is_rejected(
    client: httpx.Client,
) -> None:
    response = client.post(
        "/activity",
        json=activity_payload("CI rejected", categories=["NOT_A_CATEGORY"]),
    )

    assert response.status_code == 400, response.text


def test_an_unknown_activity_is_not_found(client: httpx.Client) -> None:
    response = client.get(f"/activity/{uuid.uuid4()}")

    assert response.status_code == 404


# ------------------------------------ endpoint 2: search with QUERY /activity


def test_a_text_search_finds_the_created_activity(
    client: httpx.Client,
    activity: dict[str, Any],
) -> None:
    response = client.request(
        "QUERY",
        "/activity",
        json={
            "text": activity["name"],
            "location": {"country": "australia", "city": "sydney"},
            "categories": {"codes": ["ADVENTURE"]},
            "price": {"max": "100.00"},
            "party_size": 4,
        },
    )

    assert response.status_code == 200, response.text
    page = response.json()
    assert [found["id"] for found in page["activities"]] == [activity["id"]]
    assert page["total"] == 1


def test_a_search_outside_the_filters_excludes_the_activity(
    client: httpx.Client,
    activity: dict[str, Any],
) -> None:
    response = client.request(
        "QUERY",
        "/activity",
        json={"text": activity["name"], "party_size": 20},
    )

    assert response.status_code == 200, response.text
    assert response.json()["total"] == 0


def test_a_search_with_an_unsupported_category_is_rejected(
    client: httpx.Client,
) -> None:
    response = client.request(
        "QUERY",
        "/activity",
        json={"categories": {"codes": ["NOT_A_CATEGORY"]}},
    )

    assert response.status_code == 400, response.text
