from django import forms
from django_ace import AceWidget


class TemplateForm(forms.Form):
    content = forms.CharField(widget=AceWidget(theme='twilight'))
