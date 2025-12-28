from unittest.mock import Mock
from src.entities.user import User
from src.repositories.user_repository_interface import UserRepositoryInterface
from src.use_cases.saving_use_case import SavingUseCase


def test_saving_user_is_calling_delegated_repository():
    # Arrange
    user = User(first_name="Abdelhakim", last_name="Berrim")
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_called_once()

def test_saving_user_save_the_user_in_the_repository():
    # Arrange
    user = User(first_name="Abdelhakim", last_name="Berrim")
    spy_user_repository = Mock(spec=UserRepositoryInterface)

    saving_use_case = SavingUseCase(user_repository=spy_user_repository)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_called_once_with(user)