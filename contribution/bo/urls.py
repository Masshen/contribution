from rest_framework import routers
from .views import MediaViewSet,AppViewSet,LanguageViewSet,SequenceViewSet

router = routers.DefaultRouter()

router.register(r'medias', MediaViewSet,'medias')
router.register(r'sequences', SequenceViewSet,'sequence')
router.register(r'apps', AppViewSet,'apps')
router.register(r'langs', LanguageViewSet,'lang')


urlpatterns = router.urls