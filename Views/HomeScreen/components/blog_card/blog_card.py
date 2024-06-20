from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty,NumericProperty,ObjectProperty
from Utils.settings import app_env
import os
from datetime import datetime

class BlogPostCard(MDBoxLayout):
    title = StringProperty()
    image = StringProperty()
    created_at = StringProperty(defaultvalue=datetime.now().strftime("%a %H:%M"))
    description = StringProperty()
    likes = NumericProperty()

    controller = ObjectProperty()

    def on_read_more(self,): 
        ...
    

    def on_heart_button(self,):
        ...