from fastapi import FastAPI
from pydantic import BaseModel

from src.controllers.saving_user_controller import SavingUserController
from src.infrastructure.mysql_user_repository import MySQLUserRepository
from src.presenters.saving_user_presenter import SavingUserPresenter
from src.use_cases.saving_use_case import SavingUseCase
from src.entities.user import User

app = FastAPI()


# ===== Request DTO (FastAPI only) =====
class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str


# ===== Infrastructure detail =====
class FakeMySQLClient:
    def insert_user(self, user: User) -> None:
        pass


# ===== Composition Root =====
def build_saving_user_controller() -> SavingUserController:
    db_client = FakeMySQLClient()
    user_repository = MySQLUserRepository(db_client=db_client)
    presenter = SavingUserPresenter()
    use_case = SavingUseCase(
        user_repository=user_repository,
        presenter=presenter,
    )
    return SavingUserController(saving_use_case=use_case)


controller = build_saving_user_controller()


# ===== API Endpoint =====
@app.post("/users")
def create_user(request: CreateUserRequest):
    view_model = controller.handle(
        first_name=request.first_name,
        last_name=request.last_name,
    )
    return {
        "full_name": view_model.full_name
    }
