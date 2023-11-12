from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Sharedpicture  # Import your model


class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=["username","email","password1","password2"]

# class SharePictureForm(forms.Form):
#     receiver = forms.ModelChoiceField(queryset=User.objects.all(), empty_label="Select a receiver")
#     picture = forms.ImageField()        

class SharePictureForm(forms.ModelForm):  # Change to forms.ModelForm
    class Meta:
        model = Sharedpicture  # Specify the model
        fields = ['receiver', 'picture']  # Include the fields you want in the form