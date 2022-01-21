from src.managers.phone_number.phone_number_manager_interface import IPhoneNumberManager
from src.models.phone_number import PhoneNumber
from src.utils.database import get_connection
from src.utils.exceptions import PhoneNumberNotFoundException

class PhoneNumberManager(IPhoneNumberManager):

    @staticmethod
    def get_by_phone_id(phone_id: int) -> PhoneNumber:
        # With the original queries we had some security issues like
        # SQL injctions. This change add more security to queries
        query = 'select "number" from phone_number where phone_id = :phone_id'
        result = get_connection().cursor().execute(query, {"phone_id": phone_id})
        if not result:
            raise PhoneNumberNotFoundException(phone_id)
        return PhoneNumber(
            number=result[0][0]
        )
