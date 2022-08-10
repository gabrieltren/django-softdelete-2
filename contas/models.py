from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.


class UsuarioManager(BaseUserManager):
    use_in_migrations = True
    
    def _create_user(self, cpf, email, password, **extra_fields):
        if not email:
            raise ValueError('O email é obrigátorio')
        
        if not cpf:
            raise ValueError('O cpf é obrigátorio')
        email = self.normalize_email(email)
        user = self.model(
            cpf = cpf, email = email, username =email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, cpf, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(cpf, email, password, **extra_fields)
    
    def create_superuser(self, cpf, email, password, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')
        return self._create_user(cpf, email, password, **extra_fields)
        
        
    
class Usuario(AbstractUser):
    email = models.EmailField("Email", max_length=255, unique=True)
    cpf = models.CharField("CPF", max_length=25, blank=True, null=True, unique=True)
    telefone = models.CharField("Telefone", max_length=25, blank=True, null=True)
    is_staff = models.BooleanField('Staff', default=False)
    
    objects = UsuarioManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['cpf']
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    
    def __str__(self):
        return f"{self.id} - {self.email}"