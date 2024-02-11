from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecordView.as_view(), name="get-record"),
    path('profile/', views.RecordProfileView.as_view(), name="get-record-profile"),
]
