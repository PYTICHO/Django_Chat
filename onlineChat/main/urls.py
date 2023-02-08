from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("newChat", views.newChat, name="newChat"),
    path("chats", views.Chats, name="Chats"),
    path("chats/<int:pk>", views.ReadyChat, name="ReadyChat"),
    path("login/<int:pk>",views.loginChat, name="loginChat")
         
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)