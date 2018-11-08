
from django import forms

class Screen_Name_Form(forms.Form):
    screen_name = forms.CharField(label='Screen Name', max_length=100)