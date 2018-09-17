from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('addUser/', include('addUser.urls')),
    path('addProject/', include('addProject.urls')),
    path('settings/', include('settings.urls')),
    path('conditions/', include('conditions.urls'))
    ]