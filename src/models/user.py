
class User:

    def __init__(self, first_name: str, last_name: str, phone_numbers: list, service_link: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone_numbers = phone_numbers
        self.service_link = service_link