from Views.CardDetailsScreen.card_details_screen import CardDetailsScreenView
from Utils.settings import storage

class CardDetailsScreenController:
    def __init__(self,model) -> None:
        self.model = model
        self.view = CardDetailsScreenView(model=model,controller=self)
    
    def get_view(self,) -> CardDetailsScreenView:
        return self.view

    def generate_card_details(self,):
        if storage.exists('active_card'):
            data = storage.get('active_card')
            self.view.ids.title.text = data.get('title')
            self.view.ids.description.text = data.get('description')
            self.view.ids.image.source = data.get('image')
            self.view.ids.created_at.text = data.get('created_at')
    
    def on_arrow_left(self,):
        self.view.ids.title.text = ''
        self.view.ids.description.text = ''
        self.view.ids.image.source = ''
        self.view.ids.title.created_at = ''
        storage.delete('active_card') 
