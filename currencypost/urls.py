from django.urls import path
from currencypost import views

urlpatterns = [
    path('currencyposts/', views.CurrencyPostList.as_view()),
]
