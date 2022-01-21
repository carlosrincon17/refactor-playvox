from src.models.user_profile import UserProfile
from src.services.send_profile_notification_interface import ISendProfileNotificationService


# Creating a controlled we can reuse the code to send notification to profiles from multiples places, like
# other scritps, etc...
class ProfileNotificationController:

    def __init__(
        self, 
        send_profile_notification_service: ISendProfileNotificationService,
    ):
        self.send_profile_notification_service = send_profile_notification_service

    def send_notifications(self, user_profiles: list[UserProfile]):
        self.send_profile_notification_service.send_notifications(
            user_profiles=user_profiles
        )

