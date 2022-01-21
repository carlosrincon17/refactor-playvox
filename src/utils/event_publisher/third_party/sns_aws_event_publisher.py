from src.utils.event_publisher.event_publisher_interface import IEventPublisher
from src.utils.event_publisher.third_party.sns_helper import SNSHelper

# Create a singleton with the connection to boto3, to avoid to create it each time.
# Implementation of Message publisher por AWS SNS, using the Singleton pattern.
class SNSAWSEventPublisher(IEventPublisher):

    __instance = None

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):      
        if(self.__initialized): return
        self.__initialized = True
        self.__client =  SNSHelper.get_sns_client()

    def publish_message(self, message):
        self.__client.client.publish(
            PhoneNumber=message["number"],
            Message=message["message"]
        )