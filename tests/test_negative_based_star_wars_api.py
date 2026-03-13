from unittest.mock import patch, MagicMock
import requests
from app.star_wars_api import fetch_data

def test_negative_invalid_option():
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = requests.HTTPError("404")

    with patch("requests.get", return_value=mock_response):
        data = fetch_data("invalid")

    assert data is None

def test_negative_empty_option():
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = requests.HTTPError("404")

    with patch("requests.get", return_value=mock_response):
        data = fetch_data("")

    assert data is None