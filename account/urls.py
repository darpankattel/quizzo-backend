from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('', include('knox.urls')),
    path('register/', views.RegisterView.as_view()),
    path('profile/', views.ProfileView.as_view()),
]
