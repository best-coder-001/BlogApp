from Utils.settings import users_storage


class RegistrationScreenModel:
    """ Represents RegistrationScreen backend. """

    def __init__(self) -> None:
        self.users = users_storage.get('users')
        self.user = {}

    def set_user_data(self,key,value):
        self.user[key] = value

    def register(self):
        ...

    