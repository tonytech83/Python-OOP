class Planet:

    def __init__(self, name):
        self.name = name
        self.items: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Planet name cannot be empty string or whitespace!")

        self.__name = value
