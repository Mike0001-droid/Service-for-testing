from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet, basename='category')
router.register(r'test', views.TestViewSet, basename='test')
router.register(r'subtest', views.SubTestViewSet, basename='subtest')
router.register(r'question', views.QuestionViewSet, basename='question')
router.register(r'attempt', views.AttemptViewSet, basename='attempt')
router.register(r'attempt_list', views.AttemptListViewSet, basename='attempt_list')
router.register(r'scale', views.ScaleListViewSet, basename='scale')
router.register(r'score', views.ScoreListViewSet, basename='score')
router.register(r'answer', views.AnsListViewSet, basename='answer')
router.register(r'interpretation',
                views.InterpretationListViewSet, basename='interpretation')
app_name = 'api'
urlpatterns = router.urls
