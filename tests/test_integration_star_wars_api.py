from unittest.mock import patch, MagicMock
from app.star_wars_api import fetch_data

def test_integration_fetch_people():
    mock_response = MagicMock()
    mock_response.json.return_value = [
        {"name": "Luke Skywalker"},
        {"name": "Leia Organa"}
    ]
    mock_response.raise_for_status.return_value = None

    with patch("requests.get", return_value=mock_response):
        data = fetch_data("people")

    assert len(data) == 2
    assert data[0]["name"] == "Luke Skywalker"
    assert data[1]["name"] == "Leia Organa"