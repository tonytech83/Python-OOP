class NextIdMixin:
    @classmethod
    def get_next_id(cls):
        customer_id = cls.id
        cls.id += 1
        return customer_id
