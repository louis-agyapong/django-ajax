from django import forms
from .models import Info

class InfoModelForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "type": "text",
        "class": "form-control",
        "id": "name",
        "required": "true",
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "class": "form-control",
        "id": "email",
        "required": "true",
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control rounded",
        "id": "message",
        "required": "true",
        "rows": "9",
    }))
    agree = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        "class": "form-check-input",
        "id": "agree",
    }), required=False, initial=False)
    class Meta:
        model = Info
        fields = ("name", "email", "message", "agree", )