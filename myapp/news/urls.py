from django.urls import path
from news import views
urlpatterns = [
    path('n/',views.newstime),
    path('random/',views.random),
    path('country/',views.country),
    path('course/',views.course),
    path('teacher/',views.teacher),
    path('class/',views.DataAnalysis.as_view())
]