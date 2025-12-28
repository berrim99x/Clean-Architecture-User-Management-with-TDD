class SavingUseCase:
    def __init__(self, user_repository, presenter):
        self.user_repository = user_repository
        self.presenter = presenter

    def execute(self, user):
        self.user_repository.save(user)
        self.presenter.present(user)
