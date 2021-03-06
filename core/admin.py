from django.contrib import admin
from core.models import Evento, Profile, UserFeed

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento',)

admin.site.register(Evento, EventoAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'birthday', 'about_me')
    list_filter = ('usuario', 'birthday')

admin.site.register(Profile, ProfileAdmin)

class UserFeedAdmin(admin.ModelAdmin):
    list_display = ('user_post', 'date_post', 'usuario')
    list_filter = ('date_post', 'usuario')

admin.site.register(UserFeed, UserFeedAdmin)
