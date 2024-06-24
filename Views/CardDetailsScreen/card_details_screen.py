from Views.base_screen import BaseScreenView


class CardDetailsScreenView(BaseScreenView):
    def on_enter(self):
        self.controller.generate_card_details()