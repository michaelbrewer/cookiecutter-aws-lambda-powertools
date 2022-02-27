from unittest.mock import MagicMock, patch

from botocore.stub import ANY, Stubber

from src.hello import app


@patch("urllib.request.urlopen")
def test_lambda_handler(mock_request: MagicMock, mock_event, lambda_context):
    stubber = Stubber(app.s3)
    expected_params = {"Body": ANY, "RequestRoute": "io-iad-cell001", "RequestToken": "token-123412341234"}
    stubber.add_response("write_get_object_response", {}, expected_params)
    stubber.activate()

    ret = app.lambda_handler(mock_event, lambda_context)
    expected = {"status_code": 200}
    assert ret == expected
