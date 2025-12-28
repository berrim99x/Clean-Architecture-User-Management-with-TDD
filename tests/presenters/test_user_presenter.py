from src.entities.user import User

class UserViewModel:
    def __init__(self, full_name: str):
        self.full_name = full_name



class UserPresenter:
    def present(self, user: User) -> UserViewModel:
        full_name = f"{user.first_name} {user.last_name}"
        return UserViewModel(full_name=full_name)


def test_user_presenter_creates_view_model():
    # Arrange
    presenter = UserPresenter()
    user = User(first_name="Abdelhakim", last_name="Berrim")

    # Act
    view_model = presenter.present(user)

    # Assert
    assert isinstance(view_model, UserViewModel)
    assert view_model.full_name == "Abdelhakim Berrim"
