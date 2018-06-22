from django import forms

class SignupForm(forms.Form):
    # max len of mc username is 16 characters
    username = forms.CharField(label="username", max_length=20) 
    email = forms.EmailField()
    password = forms.CharField(min_length=6, label="password",
                                widget=forms.PasswordInput)
    repwd = forms.CharField(min_length=6, label="repwd",
                                widget=forms.PasswordInput)

    def clean(self):
    	cleaned_data = super(SignupForm, self).clean()
    	password = self.cleaned_data.get('password')
    	repwd = self.cleaned_data.get('repwd')

    	if password and repwd and password != repwd:
        	raise forms.ValidationError("passwords do not match")
