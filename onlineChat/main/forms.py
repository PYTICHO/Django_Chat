from django import forms
from .models import *

def validate_password(password):
    if bool(re.search('[а-яА-Я]', password)):
        raise ValidationError("В пароле не должно быть русских символов!")


class CreateChatForm(forms.ModelForm):
    login = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input chat-login', 'id': "chat-login"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-input"}), label="Пароль", validators=[validate_password])

    class Meta:
        model = Chat
        fields = ("login", "password")


class CreateMessageForm(forms.ModelForm):
    text = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-input', 'id': 'form-input','placeholder': "Message...", 'autocomplete': "off"}))

    class Meta:
        model = Message
        fields = ("text",)






