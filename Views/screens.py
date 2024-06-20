from Controllers.main_screen import MainScreenController
from Models.main_screen import MainScreenModel

from Controllers.registration_screen import RegistrationScreenController
from Models.registration_screen import RegistrationScreenModel

from Controllers.home_screen import HomeScreenController
from Models.home_screen import HomeScreenModel


screens = {
    'home screen': {
        'controller': HomeScreenController,
        'model': HomeScreenModel,
    },
    'registration screen': {
        'controller': RegistrationScreenController,
        'model': RegistrationScreenModel,
    },
    'main screen': {
        'controller': MainScreenController,
        'model': MainScreenModel,
    }
}
