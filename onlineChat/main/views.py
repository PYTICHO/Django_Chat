from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.http import JsonResponse
import json, uuid
# Create your views here.

def main(request):
    context = {

    }
    return render(request, "main/main.html", context)



def newChat(request):
    if request.method == "POST":
        form = CreateChatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            login = request.POST.get("login")
            password = request.POST.get("password")

            pk = Chat.objects.get(login=login).pk
            response = redirect("ReadyChat", pk)
            response.set_cookie(f"Chat_{str(pk)}", password)
            return response
    else:
        form = CreateChatForm()

    # Существует ли логин
    loginValue = request.GET.get("loginValue", None)

    if Chat.objects.filter(login=loginValue).first():
        return JsonResponse(data={
            "loginExists": "Такой логин уже существует"
        }, status=201)
    

    context = {
        "form": form,
    }
    return render(request, 'main/newChat.html', context)




def Chats(request):
    error = ''
    chats = Chat.objects.all()
    

    if request.method == "GET":
        loginValue = request.GET.get("loginValue")

        if not loginValue:
            loginValue = ''

        if len(loginValue) > 0:
            chats = Chat.objects.filter(login__icontains=loginValue) 
            


    if len(chats) == 0:
        error = "Ничего не найдено"

    context = {
        "chats": chats,
        "error": error
    }

    return render(request, "main/Chats.html", context)




def ReadyChat(request, pk):
    login = Chat.objects.get(pk=pk).login
    form = CreateMessageForm()
    chat = get_object_or_404(Chat, login=login)
    messages = Message.objects.filter(chat__login = login)

    cookies = request.COOKIES
    try:
        sessionId = cookies["sessionid"]
    except:
        sessionId = str(uuid.uuid4())
        response = redirect("ReadyChat", pk)
        response.set_cookie("sessionid", sessionId)
        return response

    
    if f"Chat_{pk}" in cookies:
        if cookies[f"Chat_{pk}"] == chat.password:
            if request.method == "POST":
                form = CreateMessageForm(request.POST)

                if form.is_valid():
                    msg = form.save(commit=False)
                    msg.chat = chat
                    msg.author = sessionId
                    msg.save()

                    return redirect("ReadyChat", pk)
                
            context = {
                "chat": chat,
                "messages": messages,
                "form": form,
                "mySessionId": sessionId,
            }
            
            return render(request, "main/ReadyChat.html", context)
    return redirect("loginChat", pk)

            
        


    




def loginChat(request, pk):
    login = Chat.objects.get(pk=pk).login
    chat = get_object_or_404(Chat, login=login)
    cookies = request.COOKIES

    context = {
        "chat": chat,
        "errors": None
    }

    if f"Chat_{pk}" in cookies:
        if cookies[f"Chat_{pk}"] == chat.password:
            return redirect("ReadyChat", pk)
    
    if request.method == "POST":
        if request.POST.get("password") == chat.password:
            response = redirect("ReadyChat", pk)
            response.set_cookie(f"Chat_{str(pk)}", chat.password)
            return response
        context["errors"] = True
    return render(request, "main/loginChat.html", context)

    