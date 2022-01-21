# The objectes were added to encapsulate the data and make the code more redable

ACCOUNT_TYPES = {
    'user platinum': 'platinum',
    'user gold': 'gold',
    'user silver': 'silver',
    'user bronze': 'bronze',
}

class UserProfile:
    def __init__(self, user_type: str, user_profile_id: str) -> None:
        self.user_type = user_type
        self.user_profile_id = user_profile_id

    @property
    def account_type(self):
        return ACCOUNT_TYPES.get(self.user_type)

