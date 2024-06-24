from Views.base_screen import BaseScreenView
from .components import BlogPostCard
from kivymd.uix.transition.transition import MDSharedAxisTransition
from widgets import BlogAppNavDrawer,BlogAppBar

class HomeScreenView(BaseScreenView):
    def on_enter(self,):
        if not self.ids.cards_list.children:
            self.controller.generate_cards()

