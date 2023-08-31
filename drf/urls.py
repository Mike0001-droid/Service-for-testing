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
router = routers.DefaultRouter()
# router.register(r'user', TestViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/api/v1/user/1/test/?format=json
    path('api/v1/', include(router.urls)),
    path('api/v1/test/', TestAPIListForUsers.as_view()),
    path('api/v1/category/', CategoryAPIListForUsers.as_view()),
    path('api/v1/subtests/', SubtestAPIListForUsers.as_view()),
    path('', index, name='index'),
    path('new_signup/', vyuha.SignUpView.as_view(), name='signup'),
    path('profile', profile, name='profile'),
    path('tests/', login_required(views.test_list)),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('passing/<int:pk>', login_required(views.pass_the_test), name='pass_the_test'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIR)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  