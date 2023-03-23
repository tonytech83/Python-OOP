from abc import ABC, abstractmethod


class BaseWorker(ABC):

    @staticmethod
    @abstractmethod
    def work():
        pass


class Worker(BaseWorker):

    @staticmethod
    def work():
        print("I'm working!!")


class SuperWorker(BaseWorker):

    @staticmethod
    def work():
        print("I work very hard!!!")


class LazyWorker(BaseWorker):

    @staticmethod
    def work():
        print("Only I work in this company!")


class OtherWorker:

    @staticmethod
    def work():
        print('Not working any more!')


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, BaseWorker):
            self.worker = None
            return f'`worker` must be of type {worker}'

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()
        else:
            raise AssertionError


worker = Worker()
super_worker = SuperWorker()
lazy_worker = LazyWorker()
other_worker = OtherWorker()
manager = Manager()


for employee in [worker, super_worker, lazy_worker, other_worker]:
    try:
        manager.set_worker(employee)
        manager.manage()
    except AssertionError:
        print(f"manager fails to support {employee.__class__.__name__}....")
