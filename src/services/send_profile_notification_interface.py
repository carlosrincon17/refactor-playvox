from abc import ABC, abstractmethod
from src.models.user_profile import UserProfile

from src.utils.event_publisher.event_publisher_interface import IEventPublisher


# Interface for the service involved in the send notification. It will allow us to be decoupled of the way that we are 
# goind to use to send notification. In Example: 
# - we can create a new implentation that create chunks of N registers
#   and execute the send of notifications in a new trhead for each chunk (to improve the perfomance). 
# - We can create a implentation that sends to SQS each notification user profile, and create a Lambda function that consume 
#   it, get the users and nunber data and send the message to SNS.
class ISendProfileNotificationService(ABC):

    @abstractmethod
    def __init__(self, event_publisher: IEventPublisher) -> None:
        super().__init__()

    @abstractmethod
    def send_notifications(self, user_profiles: list[UserProfile]):
        pass