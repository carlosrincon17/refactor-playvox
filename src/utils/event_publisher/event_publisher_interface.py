# Define an interface that should be used by all the implementations
# to publish a message (In a event bus or anywhere). The script is only coupled to the interface,
# and we can create more implementation to publish messages: in kafka, SQS, RabitMQ, redis... until an API
# without impact the rest of the script

from abc import ABC, abstractmethod


class IEventPublisher(ABC):

    @abstractmethod
    def publish_message(self, message):
        pass
