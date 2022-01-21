from src.utils.event_publisher.third_party.sns_aws_event_publisher import SNSAWSEventPublisher
from src.utils.exceptions import MessageBrokerNotFound


# Factory to define which class MessagePublisher should be used, according with the type of the 
# message that we want to send
class EventPublisherFactory:

    PUBLISHERS = {
        "SNS": SNSAWSEventPublisher
    }

    @staticmethod
    def get_event_publisher(type: str) -> None:
        if type not in EventPublisherFactory.PUBLISHERS:
            raise MessageBrokerNotFound(type)
        return EventPublisherFactory.PUBLISHERS.get(type)()