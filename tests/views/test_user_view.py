from src.view_models.user_view_model import UserViewModel
from src.views.user_view import UserView


def test_view_displays_user_full_name():
    # Arrange
    view = UserView()
    view_model = UserViewModel(full_name="Abdelhakim Berrim")

    # Act
    result = view.render(view_model)

    # Assert
    assert result == "User saved: Abdelhakim Berrim"
