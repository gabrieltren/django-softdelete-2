from django.contrib import admin

from .models import Usuario
from django.contrib.auth.admin import UserAdmin
from .forms import UsuarioCreateForm, UsuarioChangeForm

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_per_page = 10
    add_form= UsuarioCreateForm
    form = UsuarioChangeForm
    model = Usuario
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'is_superuser']
    readonly_fields = ['last_login', 'date_joined',]
    fieldsets = (
        ('Login', {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name','telefone', 'cpf')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Data Importantes', {'fields': ('last_login', 'date_joined')})
    )
    
