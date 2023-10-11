from django.urls import path
from userprofile import views


urlpatterns = [
    path('profiles/', views.UserProfileList.as_view()),
]
