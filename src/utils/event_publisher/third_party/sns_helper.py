import boto3
from src.utils.config import AWSConfig

class SNSHelper():

    @staticmethod
    def get_sns_client():
        return boto3.client(
                "sns",
                aws_access_key_id=AWSConfig.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWSConfig.AWS_SECRET_ACCESS_KEY,
                region_name=AWSConfig.REGION_NAME
            )