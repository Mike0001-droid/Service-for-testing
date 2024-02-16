from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'attempt', views.AttemptViewSet, basename='attempt')
router.register(r'subtest', views.SubtestViewSet, basename='subtest')
app_name = 'api'
urlpatterns = router.urls

