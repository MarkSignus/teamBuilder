from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('associates/', include('associates.urls')),
    path('projects/', include('projects.urls')),
    path('settings/', include('settings.urls'))
    ]