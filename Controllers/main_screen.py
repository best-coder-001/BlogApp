from pydantic import ValidationError
from Views.MainScreen.main_screen import MainScreenView
from Utils.settings import logger
from Utils.utils import alert

class MainScreenController:
    def __init__(self,model) -> None:
        self.model = model
        self.view = MainScreenView(controller=self,model=model)
    
    def get_view(self) -> MainScreenView:
        return self.view
    
    def set_user_data(self,key,value):
        self.model.set_user_data(key,value)

    def clear_fields_data(self):
        self.view.ids.username.text = ''
        self.view.ids.password.text = ''

    def on_login_button(self):
        try:
            self.model.authorization()
            logger.log('info','Success login from user %s',self.model.user)
        except Exception as ex:
            logger.log('error','Login failed. Reason: %s',str(ex))
            alert('Error', "Something went wrong!")
        else:
            self.view.manager_screens.current = 'home screen'
    