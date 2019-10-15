from django.urls import path, include

urlpatterns = [
    path('room/', include('app.api.room.urls')),
    path('user/', include('app.api.user.urls')),
    path('chat/', include('app.api.chat.urls')),
    path('message/', include('app.api.message.urls')),

]