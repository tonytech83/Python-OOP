# Exam: 03. Profile
# From: Encapsulation - Lab
# URL: https://judge.softuni.org/Contests/Practice/Index/1938#2

class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @username.setter
    def username(self, value):
        """
        Checks the length of username, it should be between 5 and 15 characters (inclusive).
        """
        if len(value) < 5 or len(value) > 15:
            raise ValueError('The username must be between 5 and 15 characters.')

        self.__username = value

    @password.setter
    def password(self, value):
        """
        The password must be at least 8 characters long;
        it must contain at least one upper case letter and at least one digit
        """
        if all([
            self.check_password_len(value),
            self.check_for_capital_letter(value),
            self.check_for_digit(value),
        ]):
            self.__password = value
            return

        raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')

    @staticmethod
    def check_password_len(value):
        return len(value) >= 8

    @staticmethod
    def check_for_capital_letter(value):
        return any([char.isupper() for char in value])

    @staticmethod
    def check_for_digit(value):
        return any(char.isdigit() for char in value)

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


# Test code 1
profile_with_invalid_password = Profile('My_username', 'My-password')

# Test code 2
profile_with_invalid_username = Profile('Too_long_username', 'Any')

# Test code 3
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
