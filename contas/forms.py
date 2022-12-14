from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario
from django import forms


class UsuarioCreateForm(UserCreationForm):
    telefone = forms.CharField(max_length=25)
    class Meta:
        fields = ['fist_name', 'last_name', 'cpf', 'telefone']
        labels = {'username': 'Usuario/Email'}
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['username']
        if commit:
            user.save()
        return user
    
class UsuarioChangeForm(UserChangeForm):
    
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name','cpf', 'telefone']