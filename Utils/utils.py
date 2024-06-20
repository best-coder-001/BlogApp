import json
from pydantic import BaseModel, field_validator, ValidationError
from Utils.validation import UsernameValidator,PasswordValidator
from kivy.metrics import dp
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogIcon,
    MDDialogHeadlineText,
    MDDialogSupportingText,
    MDDialogButtonContainer,
    MDDialogContentContainer,
)

class RegistrationForm(BaseModel):
    username: str
    password1: str
    password2: str


    @field_validator('username')
    @classmethod
    def validate_username(cls, v): 
        UsernameValidator(value=v)
        return v
    
    @field_validator('password1')
    @classmethod
    def validate_psw1(cls, v,): 
        PasswordValidator(value=v)
        return v
    
    @field_validator('password2')
    @classmethod
    def passwords_match(cls, v, info):
        if 'password1' in info.data and v != info.data['password1']:
            raise ValueError('passwords do not match')
        return v
    

class UserLoginForm(BaseModel):
    username: str
    password: str

    @field_validator('username')
    @classmethod
    def validate_username(cls, v): 
        UsernameValidator(value=v)
        return v
    
    @field_validator('password')
    @classmethod
    def validate_psw1(cls, v,): 
        PasswordValidator(value=v)
        return v
    

def authenticate(users: list[dict,],user: dict):
    for _user in users:
        if _user['username'] == user['username'] or _user['password'] == user['password']:
            return True

def create_user(username,password):
    """ TODO: Implement creating new user. """
    user = {
        'username': username,
        'password': password,
        'is_online': False
    }

def login(users: list[dict,],user: dict):
    if not authenticate(users,user):
        raise ValueError('Login failed. Cant find user like this.')
    else:
        """ TODO: Implement user logging by turning is_online.  """

    
def register(users: list[dict,],user: dict,users_path: str):
    """ TODO: Implement changing user status  """
    if not authenticate(users,user):
        users.append(user)
        with open(users_path,'w') as file:
            file.write(json.dumps(users,indent=4))
    else:
        raise ValueError('Registration failed.User like this already exist.')

def logout(users: list[dict,],user: dict,users_path):
    ...

  
def alert(title,msg):
    dialog = MDDialog(
        # -----------------------Headline text-------------------------
        MDDialogHeadlineText(
            text=title,
            font_style="Title",
            role="medium"
        ),
        # -----------------------Supporting text-----------------------
        MDDialogSupportingText(
            text=msg,
            font_style="Body",
            role="medium",
        ))
    dialog.open()
    dialog.update_width()


