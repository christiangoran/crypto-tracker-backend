from django.urls import path
from favouritecurrencies import views

urlpatterns = [
    path('favouritecurrencies/', views.FavouriteCurrenciesList.as_view()),
    path('favouritecurrencies/<int:pk>/',
         views.FavouriteCurrenciesDetail.as_view()),
]
