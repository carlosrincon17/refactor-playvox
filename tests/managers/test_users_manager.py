from distutils.command.build import build
from unittest.mock import MagicMock
import mock
import pytest

from src.models.user_profile import UserProfile
from src.models.user import User
from src.managers.users.user_manager import UserManager
from src.utils.exceptions import UserNotFoundException


@mock.patch('src.managers.users.user_manager.get_connection')
def test_user_manager_get_by_profile_id_raise_not_found_execption(mock_get_connection):
    with pytest.raises(UserNotFoundException):
        db_connection = MagicMock()
        mock_get_connection.return_value = db_connection 
        mock_cursor = MagicMock()
        db_connection.cursor.return_value = mock_cursor
        mock_cursor.execute.return_value = []
        result = UserManager().get_by_profile_id(123)
        assert len(result) == 0


@mock.patch('src.managers.users.user_manager.get_connection')
def test_user_manager_get_by_profile_id(mock_get_connection, build_profile: UserProfile, build_user: User):
    db_connection = MagicMock()
    mock_get_connection.return_value = db_connection 
    mock_cursor = MagicMock()
    db_connection.cursor.return_value = mock_cursor
    mock_cursor.execute.return_value = [build_user.first_name, build_user.last_name, build_user.phone_numbers, build_user.service_link]
    result = UserManager().get_by_profile_id(build_profile.user_profile_id)
    assert result.service_link == build_user.service_link

    