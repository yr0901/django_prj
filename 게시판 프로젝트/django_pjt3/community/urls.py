from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:review_pk>/', views.detail, name='detail'),
    path('<int:pk>/update', views.update, name='update'),
    path('<int:id>/delete', views.delete, name='delete'),
    path('<int:review_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:comment_pk>/<int:review_pk>/delete/comments/', views.comments_delete, name='comments_delete'),
]