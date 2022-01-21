
from abc import ABC, abstractmethod

from src.models.user import User


class IUserManager(ABC):

    @staticmethod
    @abstractmethod
    def get_by_profile_id(profile_id: int) -> User:
        raise NotImplementedError