
# The factory with allow us to define which implementation should we use according with
# the file type. Without impact the rest of code.
from src.utils.profile_filereader.csv_file_reader import IFileProfileReader
from src.utils.profile_filereader.file_reader_interface import CsvFileProfileReader


class FileProfileReaderFactory:

    @staticmethod
    def  get_file_profile_reader(file_type: str, filename: str) -> IFileProfileReader:
        return {
            "txt": CsvFileProfileReader
        }.get(file_type, CsvFileProfileReader)(filename=filename)