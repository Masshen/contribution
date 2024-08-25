from rest_framework import routers
from .views import MediaViewSet

router = routers.DefaultRouter()

router.register(r'medias', MediaViewSet)


urlpatterns = router.urls