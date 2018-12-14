from django import forms
from .models import Student

class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'age'
        ]

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your first name here'
        }
    )
)

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Enter last name here'
        }
    )
)