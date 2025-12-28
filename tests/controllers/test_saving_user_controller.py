from unittest.mock import Mock
from src.entities.user import User
from src.use_cases.saving_use_case import SavingUseCase

class SavingUserController:
    def __init__(self, saving_use_case):
        self.saving_use_case = saving_use_case

    def handle(self, first_name: str, last_name: str) -> None:
        user = User(first_name=first_name, last_name=last_name)
        self.saving_use_case.execute(user)


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
