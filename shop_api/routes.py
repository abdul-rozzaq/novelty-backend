from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import BookCreateUpdateViewSet

router = DefaultRouter()

router.register('book', BookCreateUpdateViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('book/', BookCreateUpdateViewSet.as_view())
# ]
