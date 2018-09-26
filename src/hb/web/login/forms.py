from django import forms

class LoginForm(forms.Form):
    # max len of mc username is 16 characters
    username = forms.CharField(label="username", max_length=20) 
    email = forms.EmailField()
