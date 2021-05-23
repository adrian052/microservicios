from django.urls import path

from .views import OrderViewSet,OrderItemViewSet

urlpatterns = [
    path('order/', OrderViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('order/<str:pk>', OrderViewSet.as_view({
        'delete': 'destroy'
    })),
    path('order_item/', OrderItemViewSet.as_view({
        'post': 'create',
    })),
    path('order_item/<str:pk>', OrderItemViewSet.as_view({
        'get': 'retrive',
    }))
]