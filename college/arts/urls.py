from django.urls import path
from .views import * # . = root path
from arts.api import * # all classes imported

from . import api
from arts import api # api.py file imported



# {{base url}}/app(prefix)/about/

urlpatterns = [
    # path('Login/', Login, name='home yguuy jhiiu '),
    # path(endpoint , filename.classname, discription)
    
    
    
    # path('about/', api.about, name='about'),
    # path('about/', about, name='about'),
    # path('contact/', views.contact, name='contact'),
    # path('services/', views.services, name='services'),
    # path('products/', views.products, name='products'),
]
