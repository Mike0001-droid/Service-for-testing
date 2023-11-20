from django.contrib import admin
from django.urls import path, include
#from django.conf import settings
from drf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/test/', include('api.urls', namespace='app')),
    path('api/user/', include('users.urls', namespace='user')),
]

if settings.DEBUG:
    from rest_framework.documentation import include_docs_urls
    urlpatterns.append(path('api/', include_docs_urls(title='API docs')))
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_DIR)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)