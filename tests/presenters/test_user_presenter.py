from src.entities.user import User


class UserPresenter:
    pass


class UserViewModel:
    pass


def test_user_presenter_creates_view_model():
    # Arrange
    presenter = UserPresenter()
    user = User(first_name="Abdelhakim", last_name="Berrim")

    # Act
    view_model = presenter.present(user)

    # Assert
    assert isinstance(view_model, UserViewModel)
    assert view_model.full_name == "Abdelhakim Berrim"
