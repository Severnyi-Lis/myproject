from django import forms
from .models import Psich
class PsichForm(forms.ModelForm):
    class Meta:
        model = Psich
        fields = [field.name for field in Psich._meta.get_fields()]