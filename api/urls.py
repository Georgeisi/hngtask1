from django.urls import path,include
from . import views

urlpatterns = [
    path('' , views.home ),
    path('create/', views.get_user),
    path('persons/<int:pk>/', views.person_detail),

]
