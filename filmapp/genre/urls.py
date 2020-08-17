from django.urls import path
from genre import views


urlpatterns = [
    path('', views.ListAll.as_view()),
    path('<int:pk>', views.Detail.as_view()),
]