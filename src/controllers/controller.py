from abc import ABC, abstractmethod
from models import UserProfile
from services.send_profile_notification_interface import ISendProfileNotificationService

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

