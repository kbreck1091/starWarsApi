from unittest.mock import patch, MagicMock
import requests
from app.star_wars_api import main

def test_main_success(capsys):
    mock_response = MagicMock()
    mock_response.json.return_value = [{"name": "Luke Skywalker"}]
    mock_response.raise_for_status.return_value = None

    with patch("builtins.input", return_value="people"):
        with patch("requests.get", return_value=mock_response):
            main()

    captured = capsys.readouterr()
    assert "Luke Skywalker" in captured.out

def test_main_failure(capsys):
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = requests.HTTPError("404")

    with patch("builtins.input", return_value="people"):
        with patch("requests.get", return_value=mock_response):
            main()

    captured = capsys.readouterr()
    assert "Unable to download data" in captured.out