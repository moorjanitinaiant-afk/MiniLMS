from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','password']

    def clean(self):

        cleaned=super().clean()

        p1=cleaned.get("password")
        p2=cleaned.get("confirm_password")

        if p1!=p2:
            raise forms.ValidationError("Passwords do not match")

        return cleaned