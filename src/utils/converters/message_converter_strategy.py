from abc import ABC, abstractmethod

from src.models.phone_number import PhoneNumber
from src.models.user import User
from src.models.user_profile import UserProfile

# As we can create implementations to publish messages, each one should format the message according
# with it implemetation, We can use the Strategy pattern to decoupled the convertion of the data to message
# publised
class IMessageConverterStrategy(ABC):

    @abstractmethod
    def convert(self, phone_number: PhoneNumber, user: User,  profile: UserProfile) -> dict:
        pass