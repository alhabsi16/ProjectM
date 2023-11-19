"""
Definition of urls for KingExhibition.
"""

from datetime import datetime
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
import ecom.views

urlpatterns = [
    path('',ecom.views.home, name='home'),
    path('product/',ecom.views.product, name='product'),
    path('pro/',ecom.views.pro, name='pro'),
      path('login/',ecom.views.login, name='login'),
    path('shopping/', ecom.views.shopping, name='shopping'),
    path('cart/',ecom.views.cart, name='cart'),
    path('ab1/',ecom.views.ab1, name='about1'),
    path('contact1/',ecom.views.contact, name='contact'),
    path('checkout/',ecom.views.checkout, name='checkout'),
    path('main/',ecom.views.main, name='main'),
    path('update_item/',ecom.views.updateitem, name='update_item'),
    #path('', views.home, name='home'),
    #path('contact/', views.contact, name='contact'),
    #path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

