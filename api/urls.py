from django.contrib import admin
from django.urls import path, include
from api.views import *
from rest_framework import routers
from rest_framework_simplejwt.views import *
from django.contrib.auth.decorators import login_required
from api import views
from users import views as vyuha
from django.conf.urls.static import static
from drf import settings
app_name = 'api'

router = routers.DefaultRouter()
router.register(r'tests', views.TestAPIListForUsers, basename='tests')
router.register(r'category', views.CategoryViewSet, basename='category')
urlpatterns = router.urls
