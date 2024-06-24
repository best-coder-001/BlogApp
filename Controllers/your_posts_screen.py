from Views.YourPostsScreen.your_posts_screen import YourPostsScreenView


class YourPostsScreenController:
    def __init__(self,model) -> None:
        self.model = model
        self.view = YourPostsScreenView(controller=self,model=model)
    
    def get_view(self) -> YourPostsScreenView:
        return self.view
    

    