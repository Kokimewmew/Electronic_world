from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('electronic/', include('electronic.urls', namespace='main')),
                  path('users/', include('users.urls', namespace='users'))] + static(settings.MEDIA_URL,
                                                                                     document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
