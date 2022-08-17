from django.conf import settings
from rest_framework import serializers
from .models import Movimentacao
from contas.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    nome = serializers.SerializerMethodField()
    
    def get_nome(self, obj):
        return f"{obj.first_name} {obj.last_name}"
        
    
    class Meta:
        model = Usuario
        fields = [
            "id",
            "email",
            "nome",
            "cpf",
            "telefone"
        ]

class MovimentacaoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True, many=False)
    data = serializers.DateTimeField(format=settings.DATETIME_FORMAT_OUTPUT, read_only=True)
    created_at = serializers.DateTimeField(format=settings.DATETIME_FORMAT_OUTPUT)

    class Meta:
        model = Movimentacao
        fields = "__all__"
        
class MovimentacaoCreateSerializer(serializers.ModelSerializer):
    deleted_at = serializers.DateTimeField(read_only=True)
    uuid = serializers.UUIDField(read_only=True)
    class Meta:
        model = Movimentacao
        fields = "__all__"