from django.urls import path
from account import views
urlpatterns = [
   path('signup/',views.signup),
   path('login/',views.login),
   path('teacher/',views.teacher_info)
]