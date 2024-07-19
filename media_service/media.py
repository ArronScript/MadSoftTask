import boto3
from botocore.exceptions import NoCredentialsError


class MediaService:
    def __init__(self, endpoint_url, access_key, secret_key):
        self.s3 = boto3.client('s3', endpoint_url=endpoint_url, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    def upload_file(self, bucket_name, file_name, file_path):
        try:
            self.s3.upload_file(file_path, bucket_name, file_name)
            return True
        except NoCredentialsError:
            return False

    def delete_file(self, bucket_name, file_name):
        try:
            self.s3.delete_object(Bucket=bucket_name, Key=file_name)
            return True
        except NoCredentialsError:
            return False
media_service = MediaService(endpoint_url='http://localhost:9000', access_key='arron', secret_key='secret_arron')

