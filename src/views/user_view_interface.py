from abc import ABCMeta, abstractmethod
from src.view_models.user_view_model import UserViewModel


class UserViewInterface(metaclass=ABCMeta):
    @abstractmethod
    def render(self, view_model: UserViewModel) -> str:
        pass
