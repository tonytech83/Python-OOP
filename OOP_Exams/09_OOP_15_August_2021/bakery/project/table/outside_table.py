from project.table.table import Table


class OutsideTable(Table):

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def number_range(self):
        return range(51, 101)

    @property
    def table_type(self):
        return self.__class__.__name__
