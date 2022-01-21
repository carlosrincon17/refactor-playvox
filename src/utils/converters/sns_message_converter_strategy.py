from src.models.phone_number import PhoneNumber
from src.models.user import User
from src.models.user_profile import UserProfile
from src.utils.converters.message_converter_strategy import IMessageConverterStrategy


class SNSMessageConverterStrategy(IMessageConverterStrategy):

    def convert(self, phone_number: PhoneNumber, user: User, profile: UserProfile) -> dict:
        message = f"""
            Hey {user.first_name} {user.last_name} we have some information about your {profile.account_type} account,
            please go to {user.service_link} to get more details
        """
        return {
            "number": phone_number.number,
            "message": message
        }