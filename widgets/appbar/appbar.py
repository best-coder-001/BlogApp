from kivymd.uix.appbar import MDTopAppBar
from kivy.properties import StringProperty,ObjectProperty

class BlogAppBar(MDTopAppBar):
    title = StringProperty(defaultvalue='')
    nav = ObjectProperty()