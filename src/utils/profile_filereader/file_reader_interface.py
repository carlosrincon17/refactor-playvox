from src.utils.exceptions import FileInvalidFormatException, FileReadException
from src.models.user_profile import UserProfile
from src.utils.profile_filereader.csv_file_reader import IFileProfileReader

# Added the basic implentation to allow to read files txt
class CsvFileProfileReader(IFileProfileReader):

    SEPARATOR = ';'

    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.__validate_file()
            
    def get_profiles(self) -> list[UserProfile]:
        try:
            data = []
            with open(self.filename, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    line_data = line.split(self.SEPARATOR)
                    user_profile = UserProfile(
                        user_type=line_data[0],
                        user_profile_id=line_data[1]
                    )
                    data.append(user_profile)
            return data
        except Exception as e:
            raise FileReadException(self.filename)

    # When you are working with file is recommended to validate the integrity of the file and the data before to proccess it.
    # Lets imagine there is a method to to that here
    def __validate_file(self):
        try:
            pass
        except Exception as e:
            raise FileInvalidFormatException(self.filename)

