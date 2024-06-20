from Views.base_screen import BaseScreenView
from .components import BlogPostCard

class HomeScreenView(BaseScreenView):
    def on_enter(self,):
        self.controller.generate_cards()


