from src.controllers.controller import ProfileNotificationController, SNSMessageConverterStrategy, SendProfileNotificationService
from src.utils.event_publisher import EventPublisherFactory
from src.utils.profile_filereader.file_reader_factory import FileProfileReaderFactory




if __name__ == '__main__':
    filename = None
    file_type = None
    file_profile_reader = FileProfileReaderFactory.get_file_profile_reader(file_type=file_type)(filename=filename)
    user_profiles = file_profile_reader.get_profiles(filename=filename)
    send_profile_notification_service = SendProfileNotificationService(
        event_publisher=EventPublisherFactory.get_event_publisher("SNS"),
        message_converter_strategy=SNSMessageConverterStrategy()
    )
    profile_notification_controller = ProfileNotificationController(send_profile_notification_service=send_profile_notification_service)
    profile_notification_controller.send_notifications(
        user_profiles=user_profiles
    )