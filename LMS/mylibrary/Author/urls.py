from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet

router = DefaultRouter()
router.register(r'', AuthorViewSet, basename='author')  # Removed redundant 'authors'

urlpatterns = router.urls
