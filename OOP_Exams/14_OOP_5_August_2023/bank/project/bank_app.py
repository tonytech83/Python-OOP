from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    @property
    def valid_loan_types(self):
        return {
            "StudentLoan": StudentLoan,
            "MortgageLoan": MortgageLoan
        }

    @property
    def valid_client_types(self):
        return {
            "Student": Student,
            "Adult": Adult,
        }

    @property
    def total_clients_count(self):
        return len(self.clients)

    @property
    def total_clients_income(self):
        return sum(x.income for x in self.clients)

    @property
    def loans_count_granted_to_clients(self):
        return sum([len(c.loans) for c in self.clients])

    @property
    def granted_sum(self):
        return sum([sum([l.amount for l in c.loans]) for c in self.clients])

    @property
    def loans_count_not_granted(self):
        return len(self.loans)

    @property
    def not_granted_sum(self):
        return sum(x.amount for x in self.loans)

    @property
    def avg_client_interest_rate(self):
        return sum(c.interest for c in self.clients) / len(self.clients) if self.clients else 0

    def add_loan(self, loan_type: str):
        if loan_type not in self.valid_loan_types:
            raise Exception("Invalid loan type!")

        new_loan = self.valid_loan_types[loan_type]()
        self.loans.append(new_loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.valid_client_types:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        new_client = self.valid_client_types[client_type](client_name, client_id, income)
        self.clients.append(new_client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self.__find_client_by_id(client_id)
        loan = self.__find_loan_by_type(loan_type)

        if not self.__loan_can_be_granted(client, loan):
            raise Exception("Inappropriate loan type!")

        client.loans.append(loan)
        self.loans.remove(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client_to_remove = self.__find_client_by_id(client_id)
        if not client_to_remove:
            raise Exception("No such client!")

        if client_to_remove.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client_to_remove)

        return f"Successfully removed {client_to_remove.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        increased_loans = len([l.increase_interest_rate() for l in self.loans if l.__class__.__name__ == loan_type])

        return f"Successfully changed {increased_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        increased_rates = len([c.increase_clients_interest() for c in self.clients if c.interest < min_rate])

        return f"Number of clients affected: {increased_rates}."

    def get_statistics(self):

        result = [
            f"Active Clients: {self.total_clients_count}",
            f"Total Income: {self.total_clients_income:.2f}",
            f"Granted Loans: {self.loans_count_granted_to_clients}, Total Sum: {self.granted_sum:.2f}",
            f"Available Loans: {self.loans_count_not_granted}, Total Sum: {self.not_granted_sum:.2f}",
            f"Average Client Interest Rate: {self.avg_client_interest_rate:.2f}"
        ]

        return "\n".join(result)

    def __find_client_by_id(self, client_id):
        data = [c for c in self.clients if c.client_id == client_id]
        return data[0] if data else None

    def __find_loan_by_type(self, loan_type):
        data = [loan for loan in self.loans if loan.__class__.__name__ == loan_type]
        return data[0] if data else None

    @staticmethod
    def __loan_can_be_granted(client, loan):
        if client.__class__.__name__ == "Student" and loan.__class__.__name__ == "StudentLoan":
            return True

        if client.__class__.__name__ == "Adult" and loan.__class__.__name__ == "MortgageLoan":
            return True

        return False
