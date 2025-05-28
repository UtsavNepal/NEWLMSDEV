from .serializers import LoginSerializer
from .repositories import UserRepository


class UserService:
    def __init__(self):
        self.repo = UserRepository()
    
    def register_user(self, data):
        return self.repo.create_user(data)
    
    def login(self, data):
        serializer = LoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user_name = serializer.validated_data['user_name']
            password = serializer.validated_data['password']
            user = self.repo.authenticate_user(user_name, password)
            if not user:
                return {"error": "User not found"}
            return user