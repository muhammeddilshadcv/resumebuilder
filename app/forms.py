from django import forms
from .models import profile
from django.contrib.auth.forms import UserCreationForm
class resume_form(forms.ModelForm):
    
    class Meta:
        model = profile
        fields = "__all__"

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="email")
    class Meta(UserCreationForm.Meta):
        fields=['username','email','password1','password2']

