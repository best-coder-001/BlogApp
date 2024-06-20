import multitasking
import json
import os
from Utils.settings import logger,app_env

class HomeScreenModel:
    
    def __init__(self) -> None:
        self.data: dict
        self.load_data()

    @multitasking.task
    def load_data(self,):
        try:
            with open(os.path.join(app_env.DATA_PATH,"home.json"),'r') as file:
                self.data = json.load(file)
        except Exception as ex:
            logger.log('critical', 'Data loading failed.Reason: %s', str(ex))

