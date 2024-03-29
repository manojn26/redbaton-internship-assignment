from django import forms
from django.contrib.auth import authenticate
from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

    def login(self,request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username,password)

        return user
    

class FillUpForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user','name','email','bday']

        