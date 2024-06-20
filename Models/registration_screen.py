import json
import os
import multitasking
from Utils.settings import logger,app_env
from Utils.utils import RegistrationForm,register

class RegistrationScreenModel:
    """ Represents RegistrationScreen backend. """

    def __init__(self) -> None:
        self.users_path = os.path.join(app_env.DATA_PATH,"users.json")
        self.validator = RegistrationForm
        self.users: dict
        self.user = {}
        self.load_data()

    def set_user_data(self,key,value):
        self.user[key] = value

    @multitasking.task
    def load_data(self):
        try:
            with open(self.users_path,'r') as file:
                self.users = json.load(file)
        except Exception as ex:
            logger.log('critical', 'Data loading failed.Reason: %s', str(ex))

    def registration(self):
        validated_data = self.validator(**self.user).model_dump()

        new_user = {
            'username': validated_data['username'],
            'password': validated_data['password2']
            }
        register(self.users['users'],new_user,self.users_path)

    