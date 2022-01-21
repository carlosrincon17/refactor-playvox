from email import message


class FileReadException(Exception):
    
    def __init__(self, file_path) -> None:
        self.message = f"Error reading the file: {file_path}."
        super().__init__(self.message)


class FileInvalidFormatException(Exception):
    
    def __init__(self, file_path) -> None:
        self.message = f"Invalid file format: {file_path}."
        super().__init__(self.message)


class UserNotFoundException(Exception):
    
    def __init__(self, user_data) -> None:
        self.message = f"User was not found: {user_data}."
        super().__init__(self.message)


class PhoneNumberNotFoundException(Exception):
    
    def __init__(self, phone_data) -> None:
        self.message = f"Phone number was not found: {phone_data}."
        super().__init__(self.message)


class MessageBrokerNotFound(Exception):
    
    def __init__(self, message_broker) -> None:
        self.message = f"MessageBrokerNotFound: {message_broker}."
        super().__init__(self.message)