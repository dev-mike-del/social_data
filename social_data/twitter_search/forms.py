
from django import forms

class Screen_Name_Form(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)