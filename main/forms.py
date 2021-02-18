from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]