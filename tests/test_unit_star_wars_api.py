import requests
from unittest.mock import patch, MagicMock
from app.star_wars_api import fetch_data, main

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


def test_fetch_data_title_fallback():
    mock_response = MagicMock()
    mock_response.json.return_value = [{"title": "A New Hope"}]
    mock_response.raise_for_status.return_value = None

    with patch("requests.get", return_value=mock_response):
        data = fetch_data("films")

    assert data[0]["title"] == "A New Hope"

def test_fetch_data_unknown_fallback():
    mock_response = MagicMock()
    mock_response.json.return_value = [{}]  # no name, no title
    mock_response.raise_for_status.return_value = None

    with patch("requests.get", return_value=mock_response):
        data = fetch_data("people")

    assert data == [{}]
 
def test_fetch_data_http_error_branch():
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = requests.HTTPError("Boom")

    with patch("requests.get", return_value=mock_response):
        data = fetch_data("people")

    assert data is None