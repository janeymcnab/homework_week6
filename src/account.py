from src.profile import Profile


class Account:

    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.profiles = []


    def add_profile (self, profile):
        self.profiles.append(profile)
        return len(self.profiles)

    def return_profiles_list(self):
        return self.profiles

    def remove_profile(self, profile):
        if profile.username == profile:
            self.profiles.remove(profile)
        return len(self.profiles)
