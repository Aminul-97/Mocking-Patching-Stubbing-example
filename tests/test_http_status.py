from unittest import mock
from unittest.mock import patch
from src.http_calls import Http_calls

# Testing status with mock 
def test_http_status_w_mock(mocker):
    mocker.patch('src.http_calls.Http_calls.check_status', return_value=401)
    assert Http_calls.check_status("https://example.com") == 401

# Testing status with patch
@mock.patch("src.http_calls.Http_calls.check_status", return_value=401)
def test_http_status_w_patch(check_status):
    assert check_status("https://example.com") == 401

# Testing status with patch
@patch("src.http_calls.Http_calls.check_status", return_value=401)
def test_http_status_w_patch2(check_status):
    assert check_status("https://example.com") == 401

# Testing status with monkeypatch
def test_http_status_w_monkeypatch(monkeypatch):
    def mock_return(value):
        return 401
    
    monkeypatch.setattr(Http_calls, "check_status", mock_return)
    assert Http_calls.check_status("https://example.com") == 401
