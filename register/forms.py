from .models import Register
from django.forms import ModelForm


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ['name', 'last_name', 'car', 'phonenum',]