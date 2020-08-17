from django.urls import path
from director import views


urlpatterns = [
    path('', views.ListAll.as_view()),
    path('create', views.Create.as_view()),
    path('<int:pk>', views.Detail.as_view()),
    path('detail/<int:pk>', views.DetailLogged.as_view()),
]