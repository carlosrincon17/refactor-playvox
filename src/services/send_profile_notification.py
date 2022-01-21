from src.services.send_profile_notification_interface import ISendProfileNotificationService
from src.utils.event_publisher.event_publisher_interface import IEventPublisher
from src.utils.converters.message_converter_strategy import IMessageConverterStrategy
from src.managers.phone_number.phone_number_manager_interface import IPhoneNumberManager
from src.managers.users.user_manager_interface import IUserManager
from src.managers.phone_number.phone_number_manager import PhoneNumberManager
from src.managers.users.user_manager import UserManager
from src.models.user_profile import UserProfile
from src.models.user import User


class SendProfileNotificationService(ISendProfileNotificationService):

    def __init__(self, event_publisher: IEventPublisher, message_converter_strategy: IMessageConverterStrategy) -> None:
        super().__init__()
        self.__event_publisher = event_publisher
        self.__message_converter_strategy = message_converter_strategy

    def send_notifications(self, user_profiles: list[UserProfile]):
        # This is like the original code, but we can perform some improvements like: Get althe users with the numbers in a query 
        # using the join sentence. it wold be great if we created a chunk of the profiles before to do it :) 
        for user_profile in user_profiles:
            try:
                self.__send_user_notification(user_profile=user_profile)
            except Exception as e:
                print(f"Error sending notification. Details: {user_profile}. Error: {e}")

    def __send_user_notification(self, user_profile: UserProfile):
        users = self.__get_user_manager().get_by_profile_id(user_profile.user_profile_id)
        for user in users:
            self.__send_notification_to_phone(
                user=user,
                profile=user_profile
            )

    def __send_notification_to_phone(self, user: User, profile: UserProfile):
        for phone_id in user.phone_numbers:
            number = self.__get_phone_number_manager().get_by_phone_id(phone_id)
            self.__event_publisher.publish_message(
                message=self.__message_converter_strategy.convert(
                    phone_number=number,
                    user= user,
                    profile=profile
                )
            )

    @staticmethod
    def __get_phone_number_manager() -> IPhoneNumberManager:
        return PhoneNumberManager

    @staticmethod
    def __get_user_manager() -> IUserManager:
        return UserManager