from src.models.user_profile import UserProfile
from abc import ABC, abstractmethod

# This interface was created in order to make easy support new file types 
# like json, yml files. In that way we are decoupling the parsing of the data
# read from te file.
class IFileProfileReader(ABC):

    @abstractmethod
    def get_profiles(self) -> list[UserProfile]:
        pass
