from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'answer', views.AnswerViewSet, basename='answer')
router.register(r'summscore', views.SummScoreViewSet, basename='summscore')
app_name = 'api'
urlpatterns = router.urls

