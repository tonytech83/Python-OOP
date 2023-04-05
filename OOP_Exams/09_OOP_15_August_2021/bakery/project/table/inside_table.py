from abc import ABC

from project.table.table import Table


class InsideTable(Table):

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def number_range(self):
        return range(1, 51)

    @property
    def table_type(self):
        return self.__class__.__name__
