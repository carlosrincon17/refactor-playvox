import imp


import textwrap

from src.models.phone_number import PhoneNumber
from src.models.user import User
from src.models.user_profile import UserProfile
from src.utils.converters.sns_message_converter_strategy import SNSMessageConverterStrategy


def test_sns_converter_strategy(build_user: User, build_profile: UserProfile, build_phone_number: PhoneNumber):
    message = f"""
        Hey {build_user.first_name} {build_user.last_name} we have some information about your {build_profile.account_type} account,
        please go to {build_user.service_link} to get more details
    """
    result = SNSMessageConverterStrategy().convert(
        phone_number=build_phone_number,
        user=build_user,
        profile=build_profile
    )
    assert textwrap.dedent(message) == textwrap.dedent(result["message"])
    assert build_phone_number.number == result["number"]