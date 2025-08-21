from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from qr_scanner import views

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),  # Login/logout/reset from Django

    # path('admin/', admin.site.urls),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # Home
    path('', views.index, name='index'),

    # Floor list
    path('groundfloor/', views.groundfloor, name='groundfloor'),
    path('firstfloor/', views.firstfloor, name='firstfloor'),
    path('secondfloor/', views.secondfloor, name='secondfloor'),

    # Shops
    path('ratings/', views.shop_list, name='shop_list'),
    path('rate_shop/<int:shop_id>/', views.rate_shop, name='rate_shop'),
    path('shop_detail/<int:shop_id>/', views.shop_detail, name='shop_detail'),
    path('rated_shops/', views.rated_shops, name='rated_shops'),

    path('feedback/', views.feedback, name='feedback'),

    # Categories
    path('product/<int:pk>/', v
