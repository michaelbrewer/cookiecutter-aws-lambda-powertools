import os
import uuid

import pytest

from .util import load_event

os.environ["LOG_LEVEL"] = "DEBUG"
os.environ["POWERTOOLS_TRACE_DISABLED"] = "true"
os.environ["POWERTOOLS_SERVICE_NAME"] = "{{cookiecutter.service_name}}"
os.environ["POWERTOOLS_METRICS_NAMESPACE"] = "{{cookiecutter.project_name}}"
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"
os.environ["AWS_ACCESS_KEY_ID"] = "FAKE-KEY"
os.environ["AWS_SECRET_ACCESS_KEY"] = "FAKE-SECRET"


class MockContext(object):
    function_name = "func_name"
    invoked_function_arn = "func_arn"
    memory_limit_in_mb = 512
    aws_request_id = uuid.uuid4()


@pytest.fixture
def lambda_context():
    return MockContext()


@pytest.fixture
def mock_event():
    return load_event("event.json")

