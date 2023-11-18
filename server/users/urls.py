from rest_framework import routers
from users import views

router = routers.DefaultRouter()

router.register(r'', views.MyUserViewSet, basename='users')

app_name = 'users'
urlpatterns = router.urls
