from rest_framework import routers
from api import views
app_name = 'api'

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet, basename='category')
router.register(r'test', views.TestViewSet, basename='test')
router.register(r'subtest', views.SubTestViewSet, basename='subtest')
router.register(r'question', views.QuestionViewSet, basename='question')
router.register(r'attempt', views.AttemptViewSet, basename='attempt')
router.register(r'attempt_list', views.AttemptListViewSet, basename='attempt_list')
urlpatterns = router.urls
