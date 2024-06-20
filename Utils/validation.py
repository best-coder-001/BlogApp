class PasswordValidator:
    def __init__(self, value: str):
        # Implement your password validation logic here
        if len(value) < 8:
            raise ValueError('Password must be at least 8 characters long.')
        if not value == value.capitalize():
            raise ValueError('Password first letter must be uppercase.')

class UsernameValidator:
    def __init__(self, value):
        # Implement your username validation logic here
        if len(value) < 8:
            raise ValueError('Username must be at least 3 characters long')

