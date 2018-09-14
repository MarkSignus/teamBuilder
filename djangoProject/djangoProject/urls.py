from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('addUser/', include('addUser.urls')),
<<<<<<< HEAD
    path('addProject/', include('addProject.urls'))
=======
    path('settings/', include('settings.urls'))
>>>>>>> 193e3064bed21e961d3f6c18a2e3cb92c72e4fff
    ]