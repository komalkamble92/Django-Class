from django.urls import path
#from .views import * # . = root path
from arts.api import * # all classes imported
from . import views
from . import api
from arts import api # api.py file imported



# {{base url}}/app(prefix)/about/

urlpatterns = [
    #path('Login/', Login, name='home yguuy jhiiu '),
    #path(endpoint , filename.classname, discription)
    path('function_list/',views.function_list,name='home'),
    path('home/',views.home,name='home'),
    path('home2/',views.home2,name='home2'), 
    path('students/',views.student_list,name='student_list'),
    #path('studentcount/',views.student_count,name='studentcount')
    
    
    # path('about/', api.about, name='about'),
    # path('about/', about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('services/', views.services, name='services'),
    # path('products/', views.products, name='products'),
]
