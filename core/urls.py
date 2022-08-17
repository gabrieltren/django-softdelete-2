from .views import movimentacao, movi_api, MovimentacaoViewSet
from django.urls import path

from rest_framework.routers import SimpleRouter, DefaultRouter

router = SimpleRouter()
router.register('mov', MovimentacaoViewSet)

# router =  DefaultRouter()
# router.register('mov', MovimentacaoViewSet, 'mov')


app_name = 'core'

urlpatterns = [
    path('', movimentacao, name='movimentacao'),
    path('json/', movi_api, name='movimentacao-api')
]