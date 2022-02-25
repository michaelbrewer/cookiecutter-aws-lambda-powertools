from urllib.parse import unquote_plus

from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.utilities.data_classes import S3Event, event_source
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()
tracer = Tracer()

def do_something_with(file_name: str):
    logger.info(f"Processing {file_name}")


@tracer.capture_lambda_handler
@logger.inject_lambda_context
@event_source(data_class=S3Event)
def lambda_handler(event: S3Event, context: LambdaContext):
    bucket_name = event.bucket_name

    # Multiple records can be delivered in a single event
    for record in event.records:
        object_key = unquote_plus(record.s3.get_object.key)

        do_something_with(f"{bucket_name}/{object_key}")
