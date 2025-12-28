from src.entities.user import User
from src.use_cases.saving_user_use_case_interface import (
    SavingUserUseCaseInterface,
)


class SavingUserController:
    def __init__(self, saving_use_case: SavingUserUseCaseInterface):
        self.saving_use_case = saving_use_case

    def handle(self, first_name: str, last_name: str):
        user = User(first_name, last_name)
        return self.saving_use_case.execute(user)

