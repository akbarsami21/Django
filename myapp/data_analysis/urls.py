from django.urls import path
from data_analysis import views
urlpatterns = [
    path('data_analysis/',views.data_analysis),
]