from django.contrib import admin
from django.urls import path, include
from api.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    """ path('api/v1/userlist/', UserViewSet.as_view({'get': 'list'})),
    path('api/v1/userlist/<int:pk>/',  UserViewSet.as_view({'put': 'update'})) """,
]
