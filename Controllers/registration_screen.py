from Views.RegistrationScreen.registration_screen import RegistrationScreenView
from Utils.settings import logger
from Utils.utils import alert


class RegistrationScreenController:
    def __init__(self,model) -> None:
        self.model = model
        self.view = RegistrationScreenView(controller=self,model=model)
    
    def get_view(self) -> RegistrationScreenView:
        return self.view
    
    def set_user_data(self,key,value):
        self.model.set_user_data(key,value)


    def clear_fields_data(self):
        self.view.ids.username.text = ''
        self.view.ids.password1.text = ''
        self.view.ids.password2.text = ''

    def on_registration_button(self):
        try:
            self.model.register()
            logger.log('info','Success registration from user %s',str(self.model.user))
        except Exception as ex:
            print(ex)
            logger.log('error','Registration failed. Reason: %s',str(ex))
            alert('Error', "Something went wrong!")
        else:
            self.view.manager_screens.current = 'home screen'


        

