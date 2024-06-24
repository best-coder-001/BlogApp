from Utils.settings import users_storage


class MainScreenModel:
    """ Represents MainScreen backend. """
    def __init__(self) -> None:
        self.users = users_storage.get('users')
        self.user = {}


    def set_user_data(self,key,value):
        self.user[key] = value

    def login(self,):
        ...


    

    