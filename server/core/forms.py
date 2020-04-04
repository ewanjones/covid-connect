from django import forms


class Register(forms.Form):
    full_name = forms.CharField(max_length=100)
    nickname = forms.CharField(max_length=50)
    email = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15, required=False)
    password = forms.CharField(max_length=30)
