from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('details/<str:pk>/', views.details, name="details")

]