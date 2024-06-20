import json
import os
import multitasking
from Utils.settings import logger,app_env
from Utils.utils import login,UserLoginForm

class MainScreenModel:
    """ Represents MainScreen backend. """
    def __init__(self) -> None:
        self.validator = UserLoginForm
        self.user = {}
        self.users: dict
        self.load_data()

    def set_user_data(self,key,value):
        self.user[key] = value

    @multitasking.task
    def load_data(self):
        try:
            with open(os.path.join(app_env.DATA_PATH,"users.json"),'r') as file:
                self.users = json.load(file)
        except Exception as ex:
            logger.log('critical', 'Data loading failed.Reason: %s', str(ex))


    def authorization(self):
        validated_data = self.validator(**self.user).model_dump()
        login(self.users['users'],validated_data)


    

    