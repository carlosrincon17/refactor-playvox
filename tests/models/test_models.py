from faker import Faker
from src.models.user import User
from src.models.user_profile import UserProfile
from src.models.phone_number import PhoneNumber

fake = Faker()

def test_users_model():
    
    first_name = fake.first_name()
    last_name = fake.last_name()
    phone_number = [fake.unique.phone_number() for i in range(5)]
    service_link = fake.hostname()
    user = User(first_name=first_name, last_name=last_name, phone_numbers=phone_number, service_link=service_link)
    assert first_name == user.first_name
    assert last_name == user.last_name
    assert phone_number == user.phone_numbers
    assert service_link == user.service_link


def test_profile_module():
    user_profile_id = fake.random_number()
    user_type = fake.lexify()
    user_profile = UserProfile(user_type=user_type, user_profile_id=user_profile_id)
    assert user_profile_id == user_profile.user_profile_id
    assert user_type == user_profile.user_type


def test_phone_number():
    number = fake.phone_number()
    phone_number = PhoneNumber(number=number)
    assert number == phone_number.number
