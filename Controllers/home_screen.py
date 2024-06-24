from Views.HomeScreen.home_screen import HomeScreenView
from Views.HomeScreen.components import BlogPostCard


class HomeScreenController:
    def __init__(self,model) -> None:
        self.model = model
        self.view = HomeScreenView(controller=self,model=model)


    def get_view(self) -> HomeScreenView:
        return self.view


    def generate_cards(self,):
        for card in self.model.data:
            self.view.ids.cards_list.add_widget(BlogPostCard(
                title=card['title'],
                image=card['image'],
                description=card['description'],
                likes=card['likes'],
                controller=self
            ))
    

    