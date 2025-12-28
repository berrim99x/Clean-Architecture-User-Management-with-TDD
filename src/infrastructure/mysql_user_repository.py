from src.entities.user import User
from src.repositories.user_repository_interface import UserRepositoryInterface


class MySQLUserRepository(UserRepositoryInterface):
    def __init__(self, db_client) -> None:
        self.db_client = db_client

    def save(self, user: User) -> None:
        self.db_client.insert_user(user)
