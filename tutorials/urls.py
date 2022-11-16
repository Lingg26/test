from django.urls import path
from . import views
urlpatterns = [
    path('tutorials', views.ListCreateTutorialView.as_view()),
    path('tutorials/<str:pk>', views.UpdateDeleteTutorialView.as_view()),
]