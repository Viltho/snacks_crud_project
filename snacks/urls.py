from django.contrib import admin
from django.urls import path
from .views import HomePageView, AboutPageView, SnackListView, SnackDetailsView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('snacks/',SnackListView.as_view(), name="snacks"),
    path('<int:pk>/',SnackDetailsView.as_view(), name="snack_details"),
    path('create/',SnackCreateView.as_view(), name="snack_create"),
    path('update/<int:pk>',SnackUpdateView.as_view(), name="snack_update"),
    path('delete/<int:pk>',SnackDeleteView.as_view(), name="snack_delete"),
]
