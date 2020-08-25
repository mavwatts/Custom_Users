from django import forms
from custom_users_app.models import MyUser

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = MyUser
        fields = ['displayname']
    

    
