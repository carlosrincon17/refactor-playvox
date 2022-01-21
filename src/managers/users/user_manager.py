from src.utils.database import get_connection
from src.managers.users.user_manager_interface import IUserManager
from src.models.user import User
from src.utils.exceptions import UserNotFoundException


class UserManager(IUserManager):

    @staticmethod
    def get_by_profile_id(profile_id: int) -> User:
        # With the original queries we had some security issues like
        # SQL injctions. This change add more security to queries
        query = 'select * from users where profile = :profile_id'
        result = get_connection().cursor().execute(query, {"profile": profile_id})
        if not result:
            raise UserNotFoundException(profile_id)
        first_name, last_name, phone_numbers, service_link = result
        return User(
            first_name=first_name,
            last_name=last_name,
            phone_numbers=phone_numbers,
            service_link=service_link
        )
