"""bootcamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import (
    register_view,
    login_view,
    logout_view,
)

from orders.views import (
    order_checkout_view, 
    my_orders_view,
    download_order
)

from products.views import (
    featured_product_view,
    search_view,
    product_create_view,
    product_detail_view,
    product_list_view,
    product_api_detail_view,
)

from django.views.generic import TemplateView


urlpatterns = [
    path('', featured_product_view),
    path('success/', my_orders_view),
    path('orders/', my_orders_view),
    path('orders/<int:order_id>/download/', download_order),
    path('checkout/', order_checkout_view),
    path('register/', register_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('search/', search_view),
    path('products/', product_list_view),
    path('products/create/', product_create_view),
    path('products/<int:pk>/', product_detail_view),
    re_path(r'api/products/(?P<pk>\d+)/', product_api_detail_view),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
