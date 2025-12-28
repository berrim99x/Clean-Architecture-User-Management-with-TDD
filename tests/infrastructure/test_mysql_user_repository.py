from unittest.mock import Mock
from src.entities.user import User
from src.repositories.user_repository_interface import UserRepositoryInterface


class MySQLUserRepository(UserRepositoryInterface):
    def __init__(self, db_client):
        self.db_client = db_client

    def save(self, user):
        self.db_client.insert_user(user)


def test_mysql_user_repository_saves_user_using_db_client():
    # Arrange
    db_client = Mock()
    repository = MySQLUserRepository(db_client=db_client)
    user = User(first_name="Abdelhakim", last_name="Berrim")

    # Act
    repository.save(user)

    # Assert
    db_client.insert_user.assert_called_once_with(user)
