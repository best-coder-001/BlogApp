from Controllers.main_screen import MainScreenController
from Models.main_screen import MainScreenModel

from Controllers.registration_screen import RegistrationScreenController
from Models.registration_screen import RegistrationScreenModel

from Controllers.home_screen import HomeScreenController
from Models.home_screen import HomeScreenModel

from Controllers.card_details_screen import CardDetailsScreenController
from Models.card_details_screen import CardDetailsScreenModel

from Controllers.favorite_blogs_screen import FavoriteBlogsScreenController
from Models.favorite_blogs_screen import FavoriteBlogsScreenModel

from Controllers.settings_screen import SettingsScreenController
from Models.settings_screen import SettingsScreenModel

from Controllers.your_posts_screen import YourPostsScreenController
from Models.your_posts_screen import YourPostsScreenModel

from Controllers.profile_screen import ProfileScreenController
from Models.profile_screen import ProfileScreenModel

screens = {
        'registration screen': {
        'controller': RegistrationScreenController,
        'model': RegistrationScreenModel,
    },
    'main screen': {
        'controller': MainScreenController,
        'model': MainScreenModel,
    },
    'home screen': {
        'controller': HomeScreenController,
        'model': HomeScreenModel,
    },
    'card details screen': {
        'controller': CardDetailsScreenController,
        'model': CardDetailsScreenModel,
    },
    'favorite cards screen': {
        'controller': FavoriteBlogsScreenController,
        'model': FavoriteBlogsScreenModel,
    },
    'settings screen': {
        'controller': SettingsScreenController,
        'model': SettingsScreenModel,
    },
    'your posts screen': {
        'controller': YourPostsScreenController,
        'model': YourPostsScreenModel,
    },
    'profile screen': {
        'controller': ProfileScreenController,
        'model': ProfileScreenModel,
    },
}
