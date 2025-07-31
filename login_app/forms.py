from django import forms
from .models import user_post

class UserPostStatus(forms.ModelForm):
    
    class Meta:
        model = user_post
        fields = ['author',"post"]

# class UserSignUpForm(forms.ModelForm):
    
#     class Meta:
#         model = 
#         fields = ("",)
