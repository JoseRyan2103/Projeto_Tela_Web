from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        nome=request.POST.get('nome')
        email=request.POST.get('email')
        senha1=request.POST.get('senha1')
        senha2=request.POST.get('senha2')

        if senha1!=senha2:
            return HttpResponse("Sua senha incorreta.")
        else:

            meu_usuario=User.objects.create_user(nome,email,senha1)
            meu_usuario.save()
            return redirect('login')
        
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        nome=request.POST.get('nome')
        senha=request.POST.get('senha')
        usuario=authenticate(request,nome=nome,senha=senha)
        if usuario is not None:
            login(request,usuario)
            return redirect('home')
        else:
            return HttpResponse ("Nome de usuário ou senha incorreta.")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')