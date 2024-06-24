from Views.FavoriteBlogsScreen.favorite_blogs_screen import FavoriteBlogsScreenView


class FavoriteBlogsScreenController:
    def __init__(self,model) -> None:
        self.model = model
        self.view = FavoriteBlogsScreenView(controller=self,model=model)

    def get_view(self,) -> FavoriteBlogsScreenView:
        return self.view
    
    def generate_favorite_cards(self,):
        ...
    

    