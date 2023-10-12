from django.urls import path
from . import views

urlpatterns = [
    path('currencies/', views.CurrencyList.as_view(), name='currency-list'),
    path('currencies/<int:pk>/', views.CurrencyDetail.as_view(),
         name='currency-detail'),
]
