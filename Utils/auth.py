""" This module is implementation of auth utils. """
from Utils.settings import storage,users_storage
from pydantic import BaseModel, field_validator, ValidationError
from Utils.validation import UsernameValidator,PasswordValidator


class UserRegistrationForm(BaseModel):
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
    


