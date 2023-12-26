from django.urls import path
from machine_learning import views
urlpatterns = [
   path('machine/',views.machine),
   path('a/',views.about),
]