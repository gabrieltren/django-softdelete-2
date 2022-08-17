from django.shortcuts import render

from .models import Movimentacao
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q 

from .serializers import MovimentacaoSerializer, MovimentacaoCreateSerializer

from rest_framework import viewsets
from rest_framework.decorators import api_view , permission_classes

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.response import Response

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly,])
def movi_api(request):
    mov = Movimentacao.objects.all()
    serializer = MovimentacaoSerializer(mov, many=True)
    
    return Response(serializer.data)

def movimentacao(request):
    search = request.GET.get('search', None)
    filtro = Q(deleted_at=None)
    if search:
        filtro.add(Q(tipo__contains=search), Q.AND)
    mov = Movimentacao.objects.filter(filtro)

    page = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 5)
    paginator = Paginator(mov, int(page_size))
    
    
    try:
        movs = paginator.page(page)
    except PageNotAnInteger:
        movs = paginator.page(1)
    except EmptyPage:
        movs = paginator.page(paginator.num_pages)
    
    context ={
        'movs': movs
    }
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    
    return render(request,'movimentacao.html', context)


class MovimentacaoViewSet(viewsets.ModelViewSet):
    queryset = Movimentacao.objects.all()
    serializer_class = MovimentacaoCreateSerializer
    
    def get_queryset(self):
        return self.queryset.filter(deleted_at=None)
    
    def get_serializer_class(self):
        serializer_map = {
            "list": MovimentacaoSerializer,
            "retrieve": MovimentacaoSerializer,
            "create": MovimentacaoCreateSerializer,
            "update": MovimentacaoCreateSerializer
        }
        return serializer_map.get(self.action, super().get_serializer_class())