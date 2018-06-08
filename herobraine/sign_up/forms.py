from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='User Nname', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
