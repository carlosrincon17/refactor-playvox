import argparse
from src.services.send_profile_notification import SendProfileNotificationService
from src.controllers.controller import ProfileNotificationController
from src.utils.event_publisher.event_publisher_factory import EventPublisherFactory
from src.utils.profile_filereader.file_reader_factory import FileProfileReaderFactory
from src.utils.converters.sns_message_converter_strategy import SNSMessageConverterStrategy


def start_proccess(filename):
    file_type = filename.split(".")[-1]
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
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='file with the data to send notifications.')
    args = parser.parse_args()
    start_proccess(filename=args.filename)