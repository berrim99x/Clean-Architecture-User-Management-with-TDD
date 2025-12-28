from src.entities.user import User
from src.presenters.user_presenter_interface import UserPresenterInterface
from src.view_models.user_view_model import UserViewModel


class SavingUserPresenter(UserPresenterInterface):
    def present(self, user: User) -> UserViewModel:
        return UserViewModel(
            full_name=f"{user.first_name} {user.last_name}"
        )
