from django.urls import path,include
from . import views

urlpatterns = [
    # path('' , views.home ),
    path('', views.get_user),
    path('<int:pk>/', views.person_detail),
    

]
