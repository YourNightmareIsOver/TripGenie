"""Post-commit endpoint tests against the live Student 2 Compose stack.

student-2-ci.yml's compose job runs these over HTTP once the stack is ready.
An unreachable or unhealthy backend fails the suite. Ordinary pytest runs
exclude this directory through testpaths in pyproject.toml.
"""

from __future__ import annotations

import os
import uuid
from typing import TYPE_CHECKING

import httpx
import pytest

if TYPE_CHECKING:
    from collections.abc import Iterator

BASE_URL = os.environ.get("STUDENT2_ENDPOINT_BASE_URL", "http://127.0.0.1:9000")


@pytest.fixture(scope="module")
def client() -> Iterator[httpx.Client]:
    with httpx.Client(base_url=BASE_URL, timeout=10) as http:
        http.get("/health").raise_for_status()
        yield http


def accommodation_payload(**overrides: object) -> dict[str, object]:
    return {
        "name": f"CI Endpoint Stay {uuid.uuid4().hex[:12]}",
        "type": "hotel",
        "description": "Created by the post-commit endpoint tests",
        "price_per_night": 189.5,
        "availability_status": "available",
        "location_details": {"country": "australia", "city": "sydney"},
    } | overrides


@pytest.fixture
def accommodation(client: httpx.Client) -> Iterator[dict[str, object]]:
    sent = accommodation_payload()
    response = client.post("/accommodation", json=sent)
    assert response.status_code == 201, response.text
    created = response.json() | {"sent": sent}
    yield created
    # Deleting the row keeps reruns against a persistent volume clean.
    client.delete(f"/accommodation/{created['id']}")


# Endpoint 1: POST /accommodation


def test_create_accommodation_returns_201_and_reads_back(client, accommodation):
    sent = accommodation["sent"]
    assert accommodation["name"] == sent["name"]

    fetched = client.get(f"/accommodation/{accommodation['id']}")
    assert fetched.status_code == 200
    body = fetched.json()
    assert body["name"] == sent["name"]
    assert body["location_details"]["city"] == "sydney"


def test_created_accommodation_is_listed(client, accommodation):
    response = client.get("/accommodation", params={"limit": 100})
    assert response.status_code == 200
    body = response.json()
    assert body["total"] >= 1
    assert accommodation["id"] in {row["id"] for row in body["accommodations"]}


def test_create_accommodation_rejects_missing_name(client):
    payload = accommodation_payload()
    del payload["name"]
    assert client.post("/accommodation", json=payload).status_code in {400, 422}


def test_create_accommodation_rejects_unknown_city(client):
    payload = accommodation_payload(
        location_details={"country": "australia", "city": "narnia"}
    )
    assert client.post("/accommodation", json=payload).status_code == 400


# Endpoint 2: GET /accommodation/{id}


def test_get_accommodation_returns_full_message(client, accommodation):
    response = client.get(f"/accommodation/{accommodation['id']}")
    assert response.status_code == 200
    body = response.json()
    assert body["id"] == accommodation["id"]
    assert body["price_per_night"] == accommodation["sent"]["price_per_night"]
    assert body["availability_status"] == "available"


def test_get_unknown_accommodation_returns_404(client):
    assert client.get(f"/accommodation/{uuid.uuid4()}").status_code == 404


def test_deleted_accommodation_is_gone(client):
    created = client.post("/accommodation", json=accommodation_payload()).json()
    assert client.delete(f"/accommodation/{created['id']}").status_code == 204
    assert client.get(f"/accommodation/{created['id']}").status_code == 404
