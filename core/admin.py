from django.contrib import admin
from .models import Movimentacao

@admin.register(Movimentacao)
class MovimentacaoAdmin(admin.ModelAdmin):
    list_per_page = 5
    list_display = ['id', 'valor', 'tipo', 'data', 'usuario']
    readonly_fields = ['uuid',]
    exclude = ['deleted_at',]


