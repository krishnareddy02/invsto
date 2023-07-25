from django import forms
from .models import data101

class data_form(forms.Form):
    files=forms.FileField(allow_empty_file=False)
    class meta:
        model=data101
        fields='__all__'