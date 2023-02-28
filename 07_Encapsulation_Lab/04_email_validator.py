# Exam: 04. Email Validator
# From: Encapsulation - Lab
# URL: https://judge.softuni.org/Contests/Practice/Index/1938#3

from typing import List


class EmailValidator:
    def __init__(self, min_length: int, mails: List[str], domains: List[str]):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain: str) -> bool:
        return domain in self.domains

    def validate(self, email: str) -> bool:
        data = email.split('@')
        name = data[0]
        mail, domain = data[1].split('.')

        return self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
