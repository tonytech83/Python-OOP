class User:
    MAX_RATING = 10
    INCREASE_STEP = 0.5
    MIN_RATING = 0
    DECREASE_STEP = 2.0

    def __init__(self, first_name: str, last_name: str, driving_license_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.driving_license_number = driving_license_number
        self.rating = self.MIN_RATING
        self.is_blocked = False

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        if not value.strip():
            raise ValueError("First name cannot be empty!")
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        if not value.strip():
            raise ValueError("Last name cannot be empty!")
        self.__last_name = value

    @property
    def driving_license_number(self):
        return self.__driving_license_number

    @driving_license_number.setter
    def driving_license_number(self, value):
        if not value.strip():
            raise ValueError("Driving license number is required!")
        self.__driving_license_number = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if value < self.MIN_RATING:
            raise ValueError("Users rating cannot be negative!")
        self.__rating = value

    def increase_rating(self):
        self.rating += self.INCREASE_STEP
        if self.rating > self.MAX_RATING:
            self.rating = self.MAX_RATING

    def decrease_rating(self):
        if self.rating - self.DECREASE_STEP < self.MIN_RATING:
            self.rating = self.MIN_RATING
            self.is_blocked = True
        else:
            self.rating -= self.DECREASE_STEP

    def __str__(self):
        return f"{self.first_name} {self.last_name} Driving license: {self.driving_license_number} Rating: {self.rating}"
