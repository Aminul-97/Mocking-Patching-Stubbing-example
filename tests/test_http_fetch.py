from unittest import mock
from unittest.mock import patch
from src.http_calls import Http_calls

# Testing response with mock
def test_http_response_w_mock(mocker):
    mocker.patch('src.http_calls.Http_calls.fetch_data', return_value="This is a respones.")
    assert Http_calls.fetch_data("https://example.com") == "This is a respones."

# Testing response with patch
@mock.patch("src.http_calls.Http_calls.fetch_data", return_value="This is a respones.")
def test_http_response_w_patch(fetch_data):
    assert fetch_data("https://example.com") == "This is a respones."

# Testing response with patch
@patch("src.http_calls.Http_calls.fetch_data", return_value="This is a respones.")
def test_http_response_w_patch2(fetch_data):
    assert fetch_data("https://example.com") == "This is a respones."

# Testing response with monkeypatch
def test_http_response_w_monkeypatch(monkeypatch):
    def mock_return(value):
        return "This is a respones."
    
    monkeypatch.setattr(Http_calls, "fetch_data", mock_return)
    assert Http_calls.fetch_data("https://example.com") == "This is a respones."