from Utils.settings import app_config
app_config.setup()

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.transition.transition import MDSharedAxisTransition
from Views.screens import screens



class LoginUI(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = MDScreenManager(
            transition=MDSharedAxisTransition(
            duration=0.35,
            transition_axis='x'
            ))
        self.load_all_kv_files(self.directory)
        self.theme_cls.theme_style = "Dark"
        
    def build(self):
        self.generate_screens()
        return self.screen_manager
    

    def generate_screens(self,):
        for name in screens.keys():
            model = screens[name]['model']()
            controller = screens[name]['controller'](model=model)
            view = controller.get_view()
            view.name = name
            view.manager_screens = self.screen_manager
            self.screen_manager.add_widget(view)
    
    def change_screens(self,name):
        if not self.screen_manager.current == name:
            self.screen_manager.current = name

if __name__ == '__main__':
    LoginUI().run()
