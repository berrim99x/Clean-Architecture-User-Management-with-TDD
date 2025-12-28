from src.repositories.user_repository_interface import UserRepositoryInterface


class InMemoryUserRepository(UserRepositoryInterface):
    def __init__(self):
        self.users = []

    def save(self, user):
        self.users.append(user)
