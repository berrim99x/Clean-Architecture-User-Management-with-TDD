from abc import ABCMeta, abstractmethod
from src.entities.user import User


class SavingUserUseCaseInterface(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, user: User) -> None:
        pass
