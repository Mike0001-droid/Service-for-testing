from django.contrib import admin
from django.urls import path, include
from api.views import *
from rest_framework import routers
from rest_framework_simplejwt.views import *
router = routers.DefaultRouter()
router.register(r'user', TestViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/test/', TestAPIListForUsers.as_view()),
    path('api/v1/testupdate/<int:pk>/', TestAPIUpdate.as_view()),
    path('api/v1/listusers/', UserAPIList.as_view()),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_refresh'),

]
