from app.profiles.arnab import ARNAB_PROFILE
from app.profiles.tamasa import TAMASA_PROFILE


class ProfileLoader:

    def __init__(self):

        self.profiles = {
            "arnab": ARNAB_PROFILE,
            "tamasa": TAMASA_PROFILE
        }

    def get_profile(self, user: str):
        """
        Returns a single user's profile.
        Useful if you ever need it.
        """

        return self.profiles.get(user.lower(), {})

    def get_all_profiles(self):
        """
        Returns every known profile.
        Common uses this to know everyone.
        """

        return self.profiles