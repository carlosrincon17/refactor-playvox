import pytest


import pytest
from faker import Faker
from src.models.user import User
from src.models.user_profile import UserProfile
from src.models.phone_number import PhoneNumber


fake = Faker()

@pytest.fixture()
def build_user():
    first_name = fake.first_name()
    last_name = fake.last_name()
    phone_number = [fake.unique.phone_number() for i in range(5)]
    service_link = fake.hostname()
    return User(first_name=first_name, last_name=last_name, phone_numbers=phone_number, service_link=service_link)

@pytest.fixture()
def build_profile():
    user_profile_id = fake.random_number()
    user_type = fake.lexify()
    return UserProfile(user_type=user_type, user_profile_id=user_profile_id)

@pytest.fixture()
def build_phone_number():
    number = fake.phone_number()
    return PhoneNumber(number=number)

