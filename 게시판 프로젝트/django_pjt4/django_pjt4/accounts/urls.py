from django.urls import path
from . import views
app_name='accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:pk>/detail/', views.user_detail, name = 'user_detail'),
    path('<int:pk>/follow/', views.follow, name='follow'),
]