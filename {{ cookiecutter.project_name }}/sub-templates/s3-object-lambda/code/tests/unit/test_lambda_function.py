from src.{{cookiecutter.service_name}} import app


def test_lambda_handler(mock_event, lambda_context):
    ret = app.lambda_handler(mock_event, lambda_context)
    expected = None
    assert ret == expected
