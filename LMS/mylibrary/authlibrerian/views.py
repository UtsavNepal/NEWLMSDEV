from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer
from .models import User
from .serializers import RegistrationSerializer, UserSerializer
from rest_framework.permissions import AllowAny 
from .services import UserService

class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = dict(request.data) 
        user_service = UserService()
        user = user_service.register_user(data)
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user_name = serializer.validated_data['user_name']
            password = serializer.validated_data['password']
            user = User.objects.filter(user_name=user_name).first()
            if user and user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refreshToken': str(refresh),
                    'accessToken': str(refresh.access_token),
                    'userId': str(user.userId),  # Add userId (convert UUID to string)
                    'user_name': user.user_name   # Add user_name
                }, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)