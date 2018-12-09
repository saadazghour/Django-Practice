from django import forms
from .models import Article

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'price',
            'active'
        ]

    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your Title for Article'
        }
    )
)

    price = forms.DecimalField(initial=1000)