from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterUserView, LoginView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),  # JWT login endpoint
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),  #  Token refresh endpoint
]