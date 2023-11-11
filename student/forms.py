from django import forms
from .models import Reg

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Reg
        fields = ('username', 'email', 'password')  # Replace with actual field names
        widgets = {
            'password': forms.PasswordInput(),
        }
