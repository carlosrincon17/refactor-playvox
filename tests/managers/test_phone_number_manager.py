from unittest.mock import MagicMock
import mock
import pytest

from src.models.phone_number import PhoneNumber
from src.managers.phone_number.phone_number_manager import PhoneNumberManager
from src.utils.exceptions import PhoneNumberNotFoundException


@mock.patch('src.managers.phone_number.phone_number_manager.get_connection')
def test_user_manager_get_by_profile_id_raise_not_found_execption(mock_get_connection):
    with pytest.raises(PhoneNumberNotFoundException):
        db_connection = MagicMock()
        mock_get_connection.return_value = db_connection 
        mock_cursor = MagicMock()
        db_connection.cursor.return_value = mock_cursor
        mock_cursor.execute.return_value = []
        result = PhoneNumberManager().get_by_phone_id(123)
        assert len(result) == 0


@mock.patch('src.managers.phone_number.phone_number_manager.get_connection')
def test_user_manager_get_by_profile_id(mock_get_connection, build_phone_number: PhoneNumber):
    db_connection = MagicMock()
    mock_get_connection.return_value = db_connection 
    mock_cursor = MagicMock()
    db_connection.cursor.return_value = mock_cursor
    mock_cursor.execute.return_value = [[build_phone_number.number]]
    result = PhoneNumberManager().get_by_phone_id(build_phone_number)
    assert result.number == build_phone_number.number

    