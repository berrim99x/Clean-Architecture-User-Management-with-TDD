from unittest.mock import Mock


class User:
    pass


class UserRepositoryInterface:
    pass


class SavingUseCase:
    pass


def test_saving_user_is_calling_delegated_repository():
    # Arrange
    user = User(first_name="Abdelhakim", last_name="Berrim")
    spy_user_repository = Mock(spec=UserRepositoryInterface)
    saving_use_case = SavingUseCase(user_repository=spy_user_repository)

    # Act
    saving_use_case.execute(user)

    # Assert
    spy_user_repository.save.assert_called_once()
