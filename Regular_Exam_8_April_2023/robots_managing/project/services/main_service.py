from project.services.base_service import BaseService


class MainService(BaseService):

    def __init__(self, name: str):
        super().__init__(name, 30)

    @property
    def service_type(self):
        return "Main"
