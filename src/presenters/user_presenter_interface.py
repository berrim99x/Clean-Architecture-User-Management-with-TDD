from abc import ABCMeta, abstractmethod
from src.entities.user import User


class UserPresenterInterface(metaclass=ABCMeta):
    @abstractmethod
    def present(self, user: User) -> None:
        pass
