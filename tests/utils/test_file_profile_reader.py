import pytest
import os

from src.utils.profile_filereader.file_reader_factory import FileProfileReaderFactory
from src.utils.profile_filereader.csv_file_reader import IFileProfileReader
from src.utils.profile_filereader.file_reader_interface import CsvFileProfileReader
from src.utils.exceptions import FileReadException


def test_file_profile_reader_factory():
    file_profile_reader = FileProfileReaderFactory.get_file_profile_reader("txt", "fixtures/file_example.txt")
    assert isinstance(file_profile_reader, IFileProfileReader)
    assert isinstance(file_profile_reader, CsvFileProfileReader)

def test_csv_file_profile_reader_raise_file_not_fount_exception():
    with pytest.raises(FileReadException):
        file_profile_reader = FileProfileReaderFactory.get_file_profile_reader("txt", "fixtures/not_valid_file_example.txt")
        file_profile_reader.get_profiles()


def test_csv_file_profile_reader():
    path = os.path.abspath("tests/fixtures/file_example.txt")
    file_profile_reader = FileProfileReaderFactory.get_file_profile_reader("txt", path)
    profiles = file_profile_reader.get_profiles()
    assert len(profiles) == 2
    assert profiles[0].account_type == "gold"
    assert profiles[1].account_type == "platinum"


