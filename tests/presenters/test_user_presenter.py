from src.entities.user import User
from src.presenters.user_presenter import UserPresenter
from src.presenters.user_view_model import UserViewModel


def test_user_presenter_creates_view_model():
    # Arrange
    presenter = UserPresenter()
    user = User(first_name="Abdelhakim", last_name="Berrim")

    # Act
    view_model = presenter.present(user)

    # Assert
    assert isinstance(view_model, UserViewModel)
    assert view_model.full_name == "Abdelhakim Berrim"

def test_presenter_builds_user_view_model_from_user():
    # Arrange
    presenter = SavingUserPresenter()
    user = User(first_name="Abdelhakim", last_name="Berrim")

    # Act
    view_model: UserViewModel = presenter.present(user)

    # Assert
    assert view_model.full_name == "Abdelhakim Berrim"