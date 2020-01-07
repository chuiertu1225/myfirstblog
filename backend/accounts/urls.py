from django.urls import path
from accounts import views

urlpatterns = [
    path('login', views.Login.as_view()),
]
