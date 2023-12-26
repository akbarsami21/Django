from django.urls import path
from user import views
urlpatterns = [
    path('registation/',views.registation),
]