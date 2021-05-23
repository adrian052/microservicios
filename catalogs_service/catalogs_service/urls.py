
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# handler404 = 'myshop.views.error_404'
# handler500 = 'myshop.views.error_500'
# handler403 = 'myshop.views.error_403'
# handler400 = 'myshop.views.error_400'

urlpatterns = [
    path('', include('product.urls')),
]