from django.urls import path
from Blogs import views
urlpatterns = [
   path('b/',views.blog),
   path('b1/',views.blog1),
   path('b2/',views.blog2),
  
]
