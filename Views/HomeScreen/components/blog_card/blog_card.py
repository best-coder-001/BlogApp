from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty,NumericProperty,ObjectProperty
from Utils.settings import app_env,storage
import os
from datetime import datetime

class BlogPostCard(MDBoxLayout):
    title = StringProperty(defaultvalue='')
    image = StringProperty(defaultvalue='')
    created_at = StringProperty(defaultvalue=datetime.now().strftime("%a, %H:%M"))
    description = StringProperty(defaultvalue='')
    likes = NumericProperty(defaultvalue=0)
    controller = ObjectProperty()

    def on_read_more(self,app): 
        storage.put(
            'active_card',
            title=self.title,
            image=self.image,
            created_at=self.created_at,
            description=self.description,
            likes=self.likes,
            )
        if storage.exists('active_card'):
            app.change_screens('card details screen')
    

    def on_heart_button(self,):
        ...