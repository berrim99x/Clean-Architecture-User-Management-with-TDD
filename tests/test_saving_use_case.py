from abc import ABCMeta, abstractmethod
from unittest.mock import Mock
from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str


class UserRepositoryInterface(metaclass=ABCMeta):
    @abstractmethod
    def save(self, user: User) -> None:
        pass


class SavingUseCase:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, user):
        self.user_repository.save()



def test_saving_user_is_calling_delegated_repository():
    # Arrange
    user = User(first_name="Abdelhakim", last_name="Berrim")
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_called_once()
