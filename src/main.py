from src.controllers.saving_user_controller import SavingUserController
from src.entities.user import User
from src.infrastructure.mysql_user_repository import MySQLUserRepository
from src.presenters.saving_user_presenter import SavingUserPresenter
from src.use_cases.saving_use_case import SavingUseCase


class FakeMySQLClient:
    def insert_user(self, user: User) -> None:
        print(f"[MySQL] User saved: {user.first_name} {user.last_name}")


def main():
    # Infrastructure
    db_client = FakeMySQLClient()
    user_repository = MySQLUserRepository(db_client=db_client)

    # Presenter
    presenter = SavingUserPresenter()

    # Use Case
    use_case = SavingUseCase(
        user_repository=user_repository,
        presenter=presenter,
    )

    # Controller
    controller = SavingUserController(saving_use_case=use_case)

    # Simulate request
    controller.handle(
        first_name="Abdelhakim",
        last_name="Berrim",
    )


if __name__ == "__main__":
    main()
