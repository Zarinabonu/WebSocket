from django.urls import path, include

from app.api.chat import views

urlpatterns = [
    path('create/', views.ChatCreateAPIView.as_view(), name='api-user-room'),

]