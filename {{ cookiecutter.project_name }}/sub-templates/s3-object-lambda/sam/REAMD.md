# S3 Object Lambda example

## Deployment

Build:

```script
sam build
```

Guided deployment

```script
sam deploy --guided
```

Update examples, where `S3BucketName` is the outputted bucket name from sam deploy:

```script
aws s3 cp './examples/' s3://{S3BucketName} --recursive
```

Download via access point, where `S3ObjectLambdaAccessPoint` is the outputted access point name from sam deploy:

```script
aws s3api get-object --bucket '{S3ObjectLambdaAccessPoint}' --key lower.txt './upper.txt'
```

## Development

Install dev dependencies

```script
make dev
```

After initial deployment, run in watch mode (where `s3-app` is the name of the SAM app)

```script
sam sync --stack-name s3-app --watch
```

Clean up local environment

```script
make clean
```
