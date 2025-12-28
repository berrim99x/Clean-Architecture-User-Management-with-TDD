from src.views.user_view_interface import UserViewInterface
from src.view_models.user_view_model import UserViewModel


class UserView(UserViewInterface):
    def render(self, view_model: UserViewModel) -> str:
        return f"User saved: {view_model.full_name}"
