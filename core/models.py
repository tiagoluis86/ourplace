from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M Hrs')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        return self.data_evento < datetime.now()

    def get_evento_que_falta_menos_de_1h(self):
        return datetime.now() > self.data_evento - timedelta(hours=1) and datetime.now() < self.data_evento


class Profile(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Nome')
    last_name = models.CharField(max_length=100, verbose_name='Sobrenome')
    about_me = models.TextField(blank=True, null=True, verbose_name='Sobre mim')
    birthday = models.DateTimeField(null=True, verbose_name='Aniversário')
    member_since = models.DateTimeField(auto_now=True, verbose_name='Member since')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.name

    def get_birthday(self):
        return self.birthday.strftime('%d/%m/%Y %H:%M Hrs')

    def get_member_since(self):
        return self.member_since.strftime('%Y-%m-%dT%H:%M')

class UserFeed(models.Model):
    user_post = models.TextField(blank=True, null=True, verbose_name='post')
    date_post = models.DateTimeField(auto_now=True, verbose_name='posted at')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'userfeed'

class MainFeed(models.Model):
    user_post = models.ForeignKey(UserFeed, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'mainfeed'