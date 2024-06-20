from Views.HomeScreen.home_screen import HomeScreenView
from Views.HomeScreen.components import BlogPostCard
from kivymd.uix.divider import MDDivider

class HomeScreenController:
    def __init__(self,model) -> None:
        self.model = model
        self.view = HomeScreenView(controller=self,model=model)
        self.home_screen_manager = self.view.ids.home_screen_manager

    def get_view(self) -> HomeScreenView:
        return self.view
    
    def generate_cards(self,):
        for card in self.model.data['cards']:
            self.view.ids.cards_list.add_widget(BlogPostCard(
                title=card['title'],
                image=card['image'],
                description=card['description'],
                likes=card['likes'],
                controller=self
            ))
    
    def genenrate_favorite_posts(self,):
        ...

    def generate_self_posts(self,):
        ...
    
    