from django.contrib import admin
from django.urls import path, include
#from django.conf import settings
from drf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import MyTokenObtainPairView

def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/test/', include('api.urls', namespace='app')),
    path('api/user/', include('users.urls', namespace='user')),
    path('api/token/create/', MyTokenObtainPairView.as_view(), name='token_auth'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/glitchtip-debug/', trigger_error),
]

if settings.DEBUG:
    from rest_framework.documentation import include_docs_urls
    urlpatterns.append(path('api/', include_docs_urls(title='API docs')))
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_DIR)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
