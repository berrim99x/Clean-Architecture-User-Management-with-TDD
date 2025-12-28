from src.view_models.user_view_model import UserViewModel


class UserView:
    def render(self, view_model: UserViewModel) -> str:
        return f"User saved: {view_model.full_name}"



def test_view_displays_user_full_name():
    # Arrange
    view = UserView()
    view_model = UserViewModel(full_name="Abdelhakim Berrim")

    # Act
    result = view.render(view_model)

    # Assert
    assert result == "User saved: Abdelhakim Berrim"
