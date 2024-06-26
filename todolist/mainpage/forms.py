from django import forms
from .models import Task
from .models import Cat
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [field.name for field in Task._meta.get_fields()]
        labels = {
            "given": "Задача выдана",
        }
        widgets = {
            'given' :   forms.DateInput(attrs={'type':'datetime-local'}),
            'deadline': forms.DateInput(attrs={'type':'datetime-local'}),
            'category': forms.DateInput(attrs={'type':'color'}),
        }

   