from django.contrib import admin
from django.urls import path, include
from api.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', TestViewSet)
print (router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/test/', TestAPIListForUsers.as_view()),
    path('api/v1/testupdate/<int:pk>/', TestAPIUpdate.as_view())
]
