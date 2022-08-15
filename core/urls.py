from .views import movimentacao
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', movimentacao, name='movimentacao')
]