from src.entities.user import User
from src.infrastructure.in_memory_user_repository import (
    InMemoryUserRepository,
)


def test_in_memory_user_repository_saves_user():
    # Arrange
    repository = InMemoryUserRepository()
    user = User(first_name="Abdelhakim", last_name="Berrim")

    # Act
    repository.save(user)

    # Assert
    assert user in repository.users
