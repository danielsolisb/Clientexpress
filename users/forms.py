from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.db.models.base import Model
from django.forms import ModelForm
from django import forms

from .models import User


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = '__all__'
        #widgets = {
        #    'categorie': forms.Select(choices=User.options),
        #}


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

class UserProfileForm(ModelForm):
    pass

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    #Agregado 9-01-2024
    #clean email field
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('email duplicado')

    #modificamos el método save() así podemos definir  user.is_active a False la primera vez que se registra
    def save(self, commit=True):        
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.is_active = False # No está activo hasta que active el vínculo de verificación
            user.save()

        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'id_ced', 'address', 'telephone', 'country']
    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.helper = FormHelper(self)
    #    self.helper.form_method = 'post'
    #    self.helper.add_input(Submit('submit', 'Save'))