from . import  settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Auth.views import registration,login,dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/',registration,name='registration'),
    path('login/',login,name='login'),
    path('dashboard/',dashboard,name='dashboard'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
