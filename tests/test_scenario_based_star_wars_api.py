from unittest.mock import patch, MagicMock
from app.star_wars_api import fetch_data

def test_scenario_people_flow():
    mock_response = MagicMock()
    mock_response.json.return_value = [{"name": "Luke Skywalker"}]
    mock_response.raise_for_status.return_value = None

    with patch("requests.get", return_value=mock_response):
        data = fetch_data("people")

    assert data[0]["name"] == "Luke Skywalker"