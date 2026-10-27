## Student 1 post-commit endpoint tests

| Test | Result |
| --- | --- |
| `test_create_trip_returns_201_with_persisted_fields` | PASS |
| `test_created_trip_is_listed` | PASS |
| `test_create_trip_rejects_end_before_start` | PASS |
| `test_create_trip_rejects_missing_name` | PASS |
| `test_create_item_within_trip_returns_201_and_shows_on_day` | PASS |
| `test_create_item_for_unknown_trip_returns_404` | PASS |
| `test_create_item_outside_trip_dates_is_rejected` | PASS |
