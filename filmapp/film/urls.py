from django.urls import path
from film import views


urlpatterns = [
    path('', views.ListAll.as_view()),
    path('<int:pk>', views.Detail.as_view()),
    path('ratings', views.Ratings.as_view()),
    path('rate/<int:pk>', views.Rate.as_view()),
    path('list', views.UserList.as_view()),
    path('detail/<int:pk>', views.UserDetail.as_view()),
]