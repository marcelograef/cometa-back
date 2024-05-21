from django.urls import path
from .views import StockView, OrderView

urlpatterns = [
    path('order/', OrderView.as_view(), name='order'),
]
