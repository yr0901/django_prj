from django.urls import path
from . import views
app_name = 'reviews'

urlpatterns = [
    path('movie/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_pk>/create/', views.review_create, name = 'review_create'),
    path('<int:movie_pk>/<int:review_pk>/', views.review_detail, name='review_detail'),
    path('<int:movie_pk>/<int:review_pk>/update/', views.review_update, name='revuew_update'),
    path('<int:movie_pk>/<int:review_pk>/delete/', views.review_delete, name='review_delete'),
    path('<int:movie_pk>/<int:review_pk>/comment_create/', views.comment_create, name='comment_create'),
    path('<int:movie_pk>/<int:review_pk>/comment/<int:comment_pk>/delete', views.comment_delete, name='comment_delete'),
]