from django.conf.urls import url 
from .views import *
from django.urls import *
from django.conf import settings
from django.conf.urls.static import static
from Webcashier import views
app_name = 'Webcashier'
urlpatterns = [
    
    path('',loginpage ),
    path('Home/', Homepage,name='Home'),
    path('loginIncus/',loginIncus),
    path('base/',Basepage,),
    path('register/',registercus,),
    path('customers/',customers,),
    path('Incustumer/',Incustumerpage,),
    path('Editcustumer/',Editcustumerpage,),
    path('Orderhot/',Orderhotpage,),
    path('Orderblended/',Orderblendedpage,),
    path('Ordercold/',Ordercoldpage,),
    url(r'^addFace/', views.addFace),
    
    
    


]
