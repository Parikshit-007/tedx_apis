from django.urls import path
from .views import RegisterAPI, LoginAPI, TaskCreateAPI, TaskListAPI, NotificationListAPI, NotificationUpdateAPI
from knox import views as knox_views

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/tasks/', TaskListAPI.as_view(), name='tasks'),
    path('api/tasks/create/', TaskCreateAPI.as_view(), name='task-create'),
    path('api/notifications/', NotificationListAPI.as_view(), name='notifications'),
    path('api/notifications/<int:pk>/', NotificationUpdateAPI.as_view(), name='notification-update'),
]
