from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import validate_email, RegexValidator
from django.core.exceptions import ValidationError
import re

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError('Password must contain at least one uppercase letter.')
        if not re.findall('[a-z]', password):
            raise ValidationError('Password must contain at least one lowercase letter.')
        if not re.findall('[0-9]', password):
            raise ValidationError('Password must contain at least one number.')

    def get_help_text(self):
        return "Your password must contain at least one uppercase letter, one lowercase letter, and one number."

class RegistrantCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, validators=[validate_email])
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password_validator = CustomPasswordValidator()

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        # Here you can call your custom password validator
        self.password_validator.validate(password1)
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
