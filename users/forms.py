from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Repeat Password'}))

    class Meta:
        model = get_user_model()
        fields = ['email','username','password1','password2']


class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'User Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Address'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Your Bio'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone Number'}))
    occupation = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Occupation'}))
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control','placeholder':'Upload Profile Pic'}))

    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','username','email','address','phone','occupation','bio','profile_pic']
