
from django.contrib import admin
from django.urls import path, include 
from django.conf.urls import  url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Webcashier import views


urlpatterns = [
     url(r'^loginIncus$', views.loginIncus),
     path('admin/', admin.site.urls),
     path('', include('Webcashier.urls')),
     path('login',auth_views.LoginView.as_view(template_name='Webcashier/login.html'),name='login'),
     path('logout',auth_views.LoginView.as_view(template_name='Webcashier/login.html'),name='logout'),

 
   
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

