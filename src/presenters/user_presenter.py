from src.entities.user import User
from src.presenters.user_presenter_interface import UserPresenterInterface
from src.presenters.user_view_model import UserViewModel


class UserPresenter(UserPresenterInterface):
    def present(self, user: User) -> UserViewModel:
        full_name = f"{user.first_name} {user.last_name}"
        return UserViewModel(full_name=full_name)
