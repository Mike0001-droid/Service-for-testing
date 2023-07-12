from django.contrib import admin
from django.urls import path, include
from api.views import *
from rest_framework import routers
from rest_framework_simplejwt.views import *
router = routers.DefaultRouter()
router.register(r'user', TestViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/api/v1/user/1/test/
    path('api/v1/', include(router.urls)),
    path('api/v1/test/', TestAPIListForUsers.as_view()),
    path('api/v1/testupdate/<int:pk>/', TestAPIUpdate.as_view()),
    path('api/v1/listusers/', UserAPIList.as_view()),
    path('api/v1/')
]
