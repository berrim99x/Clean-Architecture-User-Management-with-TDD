from unittest.mock import Mock
from src.entities.user import User
from src.use_cases.saving_use_case import SavingUseCase
from src.controllers.saving_user_controller import SavingUserController


def test_controller_calls_saving_use_case_with_user():
    # Arrange
    spy_use_case = Mock(spec=SavingUseCase)

    controller = SavingUserController(saving_use_case=spy_use_case)

    # Act
    controller.handle(
        first_name="Abdelhakim",
        last_name="Berrim",
    )

    # Assert
    spy_use_case.execute.assert_called_once_with(
        User(first_name="Abdelhakim", last_name="Berrim")
    )
