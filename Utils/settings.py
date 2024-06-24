from typing import Optional
from kivy.config import Config
from kivy.resources import resource_add_path
from kivy.storage.jsonstore import JsonStore
from kivy.logger import Logger,LOG_LEVELS
import os


class AppConfiguration:
    def __init__(self) -> None:
        self.app_size = (420,810)
        self.is_resizable = False
        self.is_borderless = False
    def setup(self):
        Config.set('graphics','width',self.app_size[0])
        Config.set('graphics','height',self.app_size[1])
        Config.set('graphics','resizable',self.is_resizable)
        Config.set('graphics','borderless',self.is_borderless)

class AppEnviroment:
    def __init__(self) -> None:
        self.BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        self.DATA_PATH = os.path.join(self.BASE_DIR,'assets','data')
        self.IMAGE_PATH = os.path.join(self.BASE_DIR,'assets','images')
        self.setup()
        
    def setup(self,):
        resource_add_path(self.IMAGE_PATH)

class AppLogger:
    def __init__(self) -> None:
        ...

    def log(self,level: str,msg: str,*args): 
        Logger.log(LOG_LEVELS[level],msg,*args)
        
app_env = AppEnviroment()
app_config = AppConfiguration()
logger = AppLogger()

storage = JsonStore(os.path.join(app_env.DATA_PATH,'storage.json'),indent=4)
users_storage = JsonStore(os.path.join(app_env.DATA_PATH,'users.json'),indent=4)
cards_storage = JsonStore(os.path.join(app_env.DATA_PATH,'cards.json'),indent=4)