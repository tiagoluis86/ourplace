from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from core.models import Evento, Profile, UserFeed
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse

# Create your views here.



def handler404(request, exception):
    return render(request, '404.html')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/')

@login_required(login_url='/login/')
def profile(request):
    usuario = request.user
    data_atual = datetime.now() - timedelta(hours=1)
    postagem = UserFeed.objects.filter(usuario=usuario)
    profile = Profile.objects.filter(usuario=usuario)

    info = {'postagens':postagem, 'profiles':profile}

    return render(request, 'profile.html', info)

@login_required(login_url='/login/')
def submit_post(request):
    if request.POST:
        user_post = request.POST.get('user_post')
        date_post = request.POST.get('date_post')
        usuario = request.user

        id_userfeed = request.POST.get('id_userfeed')

        UserFeed.objects.create(user_post=user_post,
                                  date_post = date_post,
                                    usuario = usuario)

    return redirect('/profile/')

@login_required(login_url='/login/')
def edit_profile(request):
    id_profile = request.GET.get('id')
    info = {}
    if id_profile:
        try:
            info['profile'] = Profile.objects.get(id=id_profile)

        except Exception:
            raise Http404()

    return render(request, 'edit_profile.html', info)


@login_required(login_url='/login/')
def submit_profile(request):
    if request.POST:
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        birthday = request.POST.get('birthday')
        about_me = request.POST.get('about_me')
        usuario = request.user

        id_profile = request.POST.get('id_profile')
        if id_profile:
            profile = Profile.objects.get(id=id_profile)
            if profile.usuario == usuario:
                profile.name = name
                profile.last_name = last_name
                profile.about_me = about_me
                profile.birthday = birthday
                profile.save()

        else:
            return redirect('/profile/')


    return redirect('/profile/')


@login_required(login_url='/login/')
def friends(request):
    usuario = request.user
    return render(request, 'friends.html')

@login_required(login_url='/login/')
def communities(request):
    usuario = request.user
    return render(request, 'communities.html')

@login_required(login_url='/login/')
def feed(request):
    usuario = request.user

    postagem = UserFeed.objects.filter(usuario=usuario)

    info = {'postagens': postagem}

    return render(request, 'feed.html', info)


@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    data_atual = datetime.now() - timedelta(hours=1)
    evento = Evento.objects.filter(usuario=usuario,
                                   data_evento__gt=data_atual)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')
def lista_eventos_historico(request):
    usuario = request.user
    data_atual = datetime.now()
    evento = Evento.objects.filter(usuario=usuario,
                                   data_evento__lt=data_atual)
    dados = {'eventos':evento}
    return render(request, 'historico.html', dados)

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        try:
            dados['evento'] = Evento.objects.get(id=id_evento)
        except Exception:
            raise Http404()
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.save()

        else:
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  usuario=usuario)
    return redirect('/agenda/')

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento)
    except Exception:
        raise Http404()
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')


def json_lista_evento(request, id_usuario):
    usuario = User.objects.get(id=id_usuario)
    evento = Evento.objects.filter(usuario=usuario).values('id', 'titulo')
    return JsonResponse(list(evento), safe=False)