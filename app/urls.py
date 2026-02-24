from django.urls import path
from .views import Home
from .utils.chatendpoint import chat_view

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('chat/', chat_view, name='chat'),
]