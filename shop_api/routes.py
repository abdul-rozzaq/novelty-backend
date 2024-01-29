from .views import BookCreateUpdateViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('book', BookCreateUpdateViewSet)

urlpatterns = router.urls
