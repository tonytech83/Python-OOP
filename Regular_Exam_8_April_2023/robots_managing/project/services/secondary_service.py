from project.services.base_service import BaseService


class SecondaryService(BaseService):

    def __init__(self, name: str):
        super().__init__(name, 15)

    @property
    def service_type(self):
        return "Secondary"
