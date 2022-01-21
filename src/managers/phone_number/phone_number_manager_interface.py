from abc import ABC, abstractmethod

from src.models.phone_number import PhoneNumber


class IPhoneNumberManager(ABC):

    @staticmethod
    @abstractmethod
    def get_by_phone_id(profile_id: int) -> PhoneNumber:
        raise NotImplementedError