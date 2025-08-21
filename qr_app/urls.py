
# """
# URL configuration for qr_scanner project.
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/4.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from qr_scanner import settings
from . import views
#
urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),  # Include authentication URLs

    # path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
#index......

    path('',views.index,name='index'),

    #floorlist.....

    path('groundfloor/',views.groundfloor,name='groundfloor'),
    path('firstfloor/',views.firstfloor,name='firstfloor'),
    path('secondfloor/',views.secondfloor,name='secondfloor'),
    path('ratings/', views.shop_list, name='shop_list'),

    path('rate_shop/<int:shop_id>/', views.rate_shop, name='rate_shop'),
    path('shop_detail/<int:shop_id>/', views.shop_detail, name='shop_detail'),
    path('rated_shops/', views.rated_shops, name='rated_shops'),

    path('feedback/',views.feedback,name='feedback'),

#categorylist.....

    path('product/<int:pk>/',views.Product,name='product'),
    path('search_category/<str:pk>/', views.search_results_category, name='search_category'),

    path('fashion/', views.fashion, name='fashion'),
    path('electronic/',views.electronic,name='electronic'),
    path('food/',views.food,name='food'),
    path('cosmetics/',views.cosmetics,name='cosmetics'),
    path('jewellery/',views.jewellery,name='jewellery'),
    path('funtora/',views.funtora,name='funtora'),
    path('theater/',views.theater,name='theater'),

#shopownwer...

    path('index1/',views.index1,name='index1'),
    path('register/',views.register,name='register'),
    # path('login/',views.login,name='login'),
    path('shophome/',views.shophome,name='shophome'),
    path('viewproducts/',views.viewproducts,name='viewproducts'),

#productdetials.....

    path('clothesdetails/',views.clothesdetails,name='details'),
    path('search/', views.search_results, name='search_results'),

    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),

    # path('fooddetails/',views.fooddetails,name='fooddetails'),
    # path('electronicdetails/',views.electronicdetails,name='electronicdetails'),
    # path('parlourdetails/',views.parlourdetails,name='parlourdetails'),
    # path('funzonedetails/',views.funzonedetails,name='funzonedetails'),
    # path('theaterdetails/',views.theaterdetails,name='theaterdetails'),

#productlist....

    # path('foodlist/',views.foodview,name='foodlist'),
    # path('clothlist/',views.clothview,name='clothlist'),
    # path('electroniclist/',views.electronicview,name='electroniclist'),
    # path('parlourlist/',views.parlourview,name='parlourlist'),
    # path('funzonelist/',views.funzoneview,name='funzonelist'),
    # path('theaterlist/',views.theaterview,name='theaterlist'),
    #
    # path('addproductslink/',views.addproductslink,name='addproductslink'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
