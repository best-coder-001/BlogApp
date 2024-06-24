import multitasking
import json
import os
from Utils.settings import cards_storage

class HomeScreenModel:
    def __init__(self) -> None:
        self.data = cards_storage.get('cards')
        