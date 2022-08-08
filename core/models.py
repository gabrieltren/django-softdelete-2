from django.db import models

from django.utils import timezone
import uuid
from django.contrib.auth.models import User
from .softdelete import DeleteManager


class BaseModel(models.Model):
    class Meta:
        abstract = True
    
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)    
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)
    deleted_at = models.DateTimeField("Deletado em ", null=True, blank=True)
    
    objects = DeleteManager()
    all_objects = models.Manager()
    
    def save(self, *args, **kwargs):
        if self.uuid is None:
            self.uuid = uuid.uuid4()
        
        super(BaseModel, self).save(*args, **kwargs)
                   
        
    def delete(self, *args, **kwargs):
        self.deleted_at = timezone.now()
        self.save()
    
    def super_delete(self, *args, **kwargs):
        super(BaseModel, self).delete(*args, **kwargs)

class Movimentacao(BaseModel):
    TIPO_MOVIMENTACAO = (
        ('entrada', 'Entrada'),
        ('saida', 'Saida')
    )
    valor = models.DecimalField(decimal_places=2, max_digits=15, default=0.00)
    data = models.DateTimeField(null=True, blank=True)
    tipo = models.CharField(max_length=100, choices=TIPO_MOVIMENTACAO)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    