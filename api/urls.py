from rest_framework import routers
from api import views
app_name = 'api'

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet, basename='category')
router.register(r'test', views.TestViewSet, basename='test')
router.register(r'subtest', views.SubTestViewSet, basename='subtest')
router.register(r'question', views.QuestionViewSet, basename='question')
urlpatterns = router.urls
