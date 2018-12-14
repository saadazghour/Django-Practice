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


    # form validation
    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 18 or age > 60:
            raise forms.ValidationError("Must be between 18 and 60 ")
        return age



    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if first_name.lower() == "sazghour":
            raise forms.ValidationError("this is not a valid first name")
        return first_name