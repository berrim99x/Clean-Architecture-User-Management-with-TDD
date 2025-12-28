from src.entities.user import User
from src.repositories.user_repository_interface import UserRepositoryInterface
from src.presenters.user_presenter_interface import UserPresenterInterface
from src.use_cases.saving_user_use_case_interface import (
    SavingUserUseCaseInterface,
)


class SavingUseCase(SavingUserUseCaseInterface):
    def __init__(
        self,
        user_repository: UserRepositoryInterface,
        presenter: UserPresenterInterface,
    ):
        self.user_repository = user_repository
        self.presenter = presenter

    def execute(self, user: User):
        self.user_repository.save(user)
        return self.presenter.present(user)

