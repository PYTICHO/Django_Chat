from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
import re

# Create your models here.




class Chat(models.Model):
    login = models.CharField("Логин", max_length=300, unique=True)
    password = models.CharField("Пароль", max_length=30, blank=False, null=False)

    def get_absolute_url(self):
        return reverse('ReadyChat', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return self.login

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'

class Message(models.Model):
    chat = models.ForeignKey("Chat", on_delete=models.CASCADE)
    text = models.TextField("Текст", max_length=1000)
    author = models.CharField("Автор", max_length=1000, default="default")

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return "Chat: " + self.chat.login