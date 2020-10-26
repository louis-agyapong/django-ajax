from django import forms
from .models import Info

class InfoModelForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ("name", "email", "message", "agree", )