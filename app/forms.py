from django import forms
from app.models import UserRegister

class UserRegisterForm(forms.ModelForm):
    name = forms.CharField(label='Name')
    contact_no = forms.IntegerField(label='Contact_no')
    email_id = forms.CharField(label='Email_id')
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    class Meta:
        model = UserRegister
        fields = '__all__'