"""
URL configuration for new_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from myapp import views
# from .views import views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('about-us/',views.aboutUs),
    # path('company-details/',views.company_detail),
    # path('delear-details/',views.dealer_detail),
    # path('fieldstaff-details/',views.fieldstaff_detail),
    path('product-details/',views.product_detail),
    # path('retailer-details/',views.retailer_detail),
    path('order-details/',views.order_detail),
    path('order-item-details/',views.order_item_detail),
    path('',views.OrderManagementSystem),
    path('templates', views.Index, name='index'),
    # path('', include('account.urls')),
    
    # path('',include('capp.urls', namespace = 'capp')),
    # path('',include('dapp.urls', namespace = 'dapp')),
    # path('',include('rapp.urls', namespace = 'rapp')),
    # path('',include('fsapp.urls', namespace = 'fsapp')),
    # path('',include('myapp.urls', namespace = 'myapp')),
    
    
    
    
    
    
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)