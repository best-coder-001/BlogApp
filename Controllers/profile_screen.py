from Views.ProfileScreen.profile_screen import ProfileScreenView


class ProfileScreenController(ProfileScreenView):
    def __init__(self,model) -> None:
        self.model = model
        self.view = ProfileScreenView(controller=self,model=model)
    
    def get_view(self) -> ProfileScreenView:
        return self.view
    