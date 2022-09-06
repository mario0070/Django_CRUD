from django import forms
from .models import todos

class TodoForm(forms.ModelForm):
    class Meta:
        model=todos
        fields=["fname","lname"]