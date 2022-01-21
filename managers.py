# Crete a layer separate the access to data. The use of the interfaces will allow to 
# build a new Implementation of the manager if the datasource changes from mysql. 
# IE: another motor, an API, ...
# In that way our application is decoupled of the datasource. To code is decoupled of 
# the implementation. 

from abc import ABC, abstractmethod
from utils.database import connection
from utils.exceptions import PhoneNumberNotFoundException, UserNotFoundException
from models import PhoneNumber, User

class IUserManager(ABC):

    @staticmethod
    @abstractmethod
    def get_by_profile_id(profile_id: int) -> User:
        raise NotImplementedError

class IPhoneNumberManager(ABC):

    @staticmethod
    @abstractmethod
    def get_by_phone_id(profile_id: int) -> User:
        raise NotImplementedError


class UserManager(IUserManager):

    @staticmethod
    def get_by_profile_id(profile_id: int) -> User:
        # With the original queries we had some security issues like
        # SQL injctions. This change add more security to queries
        query = 'select * from users where profile = :profile_id'
        result = connection.execute(query, {"profile": profile_id})
        if not result:
            raise UserNotFoundException(profile_id)
        first_name, last_name, phone_numbers, service_link = result
        return User(
            first_name=first_name,
            last_name=last_name,
            phone_numbers=phone_numbers,
            service_link=service_link
        )


class PhoneNumberManager(IPhoneNumberManager):

    @staticmethod
    def get_by_phone_id(phone_id: int) -> PhoneNumber:
        # With the original queries we had some security issues like
        # SQL injctions. This change add more security to queries
        query = 'select "number" from phone_number where phone_id = :phone_id'
        result = connection.execute(query, {"phone_id": phone_id})
        if not result:
            raise PhoneNumberNotFoundException(phone_id)
        return PhoneNumber(
            number=result[0][0]
        )

