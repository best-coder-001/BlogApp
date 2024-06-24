from Views.SettingsScreen.settings_screen import SettingsScreenView


class SettingsScreenController:
    def __init__(self,model) -> None:
        self.model = model
        self.view = SettingsScreenView(controller=self,model=model)

    def get_view(self,) -> SettingsScreenView:
        return self.view
    
    def generate_settings(self,):
        ...