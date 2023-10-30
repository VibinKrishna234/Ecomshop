from django.urls import path
from . import views
from .views import products, homepage, cartlist
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('products/', views.products, name='products'),
    path('', homepage, name='homepage'),
    path('products/', products, name='products'),
    path('cart/', views.Cart, name='cart'),
    path('cart/', cartlist, name='cart_list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
