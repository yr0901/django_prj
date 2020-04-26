from django.urls import path
from . import views

app_name ='community'

urlpatterns = [
    path('', views.review_list, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.review_detail, name='detail'),
    path('<int:pk>/update/', views.review_update, name='update'),
    path('<int:pk>/delete/', views.review_delete, name='delete'),
]