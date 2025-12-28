import pytest
from unittest.mock import Mock
from src.entities.user import User
from src.repositories.user_repository_interface import UserRepositoryInterface
from src.presenters.user_presenter_interface import UserPresenterInterface
from src.use_cases.saving_use_case import SavingUseCase


def test_saving_user_is_calling_delegated_repository():
    # Arrange
    user = User(first_name="Abdelhakim", last_name="Berrim")
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    dummy_presenter = Mock(spec=UserPresenterInterface)

    saving_use_case = SavingUseCase(
        user_repository=spy_user_repository,
        presenter=dummy_presenter,
    )

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_called_once()


@pytest.mark.parametrize(
    "user",
    [
        User("Abdelhakim", "Berrim"),
        User("Islam", "Hala"),
        User("Oussama", "Khelef"),
        User("Ahmed", "Zellouma"),
    ],
)
def test_saving_user_save_the_user_in_the_repository(user):
    # Arrange
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    dummy_presenter = Mock(spec=UserPresenterInterface)

    saving_use_case = SavingUseCase(
        user_repository=spy_user_repository,
        presenter=dummy_presenter,
    )

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_called_once_with(user)


def test_saving_user_calls_presenter():
    # Arrange
    user = User(first_name="Abdelhakim", last_name="Berrim")
    dummy_user_repository = Mock(spec=UserRepositoryInterface)
    spy_presenter = Mock(spec=UserPresenterInterface)

    saving_use_case = SavingUseCase(
        user_repository=dummy_user_repository,
        presenter=spy_presenter,
    )

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_presenter.present.assert_called_once_with(user)
