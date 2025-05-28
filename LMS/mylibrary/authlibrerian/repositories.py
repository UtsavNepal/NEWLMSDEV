from .models import User
from django.contrib.auth.hashers import make_password

class UserRepository:
    def create_user(self, user_data):
        user_data["password"] = make_password(user_data["password"])
        return User.objects.create(**user_data)
    
    def authenticate_user(self, user_name, password):
        user = User.objects.filter(user_name=user_name).first()
        if user and user.check_password(password):
            return user
        return None