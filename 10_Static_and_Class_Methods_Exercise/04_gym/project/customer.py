class Customer:
    id = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.get_next_id()

    @staticmethod
    def get_next_id():
        customer_id = Customer.id
        Customer.id += 1
        return customer_id

    def __repr__(self):
        return f'Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}'
