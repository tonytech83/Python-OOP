from abc import ABC, abstractmethod


class IContent(ABC):

    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyContent(IContent):

    def format(self):
        return ''.join(['<myML>', self.text, '</myML>'])


class HTMLContent(IContent):

    def format(self):
        return ''.join(['<html>', self.text, '</html>'])


class ISender(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def format(self):
        pass


class IMSender(ISender):

    def format(self):
        return ' '.join(["I'm", self.name])


class POPSender(ISender):
    def format(self):
        return ' '.join(["P'op", self.name])


class IReceiver(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def format(self):
        pass


class IMReceiver(IReceiver):

    def format(self):
        return ' '.join(["I'm", self.name])


class POPReceiver(IReceiver):
    def format(self):
        return ' '.join(["P'op", self.name])


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass


class Email(IEmail):

    def __init__(self):
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = sender.format()

    def set_receiver(self, receiver):
        self.__receiver = receiver.format()

    def set_content(self, content):
        self.__content = content.format()

    def __repr__(self):
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


# Test code
email = Email()
im_sender = IMSender('qmal')
im_receiver = IMReceiver('james')
pop_sender = POPSender('ivan')
pop_receiver = POPReceiver('stoyan')
my_content = MyContent('Hello, there!')
html_content = HTMLContent('Hello for html!')

test_data = [
    (pop_sender, pop_receiver, my_content),
    (im_sender, im_receiver, html_content)
]

for sender, receiver, content in test_data:
    email.set_sender(sender)
    email.set_receiver(receiver)
    email.set_content(content)
    print(email)
    print()
