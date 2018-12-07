from django import forms
from .models import Product

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'descriptions', 'price', 'summary']


    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    'placeholder':'Enter Title Here'
                }
            )
        )
    
    descriptions = forms.CharField(widget=forms.Textarea(attrs={
            'placeholder' : 'Enter somthing Here',
            'rows': 8,
            'cols': 60
        }
    )
)

    price = forms.DecimalField(initial=20000)

    email = forms.EmailField()

    summary = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows':8}))

    

    # def clean_summary(self, *args, **kwargs):
    #     summary = self.cleaned_data.get('summary')
    #     print(summary)
    #     if not 'SAzghour' in summary:
    #         raise forms.ValidationError('this is not a valid summary')
    #     if not 'something' in summary:
    #         raise forms.ValidationError('this is not a valid summary')
    #     return summary



    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('com'):
            raise forms.ValidationError('This is not a valid email')
        return email




class RawCreateForm(forms.Form):
    title = forms.CharField(    
                            label='', 
                            widget=forms.TextInput(attrs={
                                'placeholder':'Enter title Here',
                            }
                        )
                    )

    descriptions = forms.CharField(
                                    required=True, 
                                    widget=forms.Textarea(
                                        attrs={
                                            'rows':10, 
                                            'cols':60, 
                                            'placeholder':'Enter somthing Here'
                                        }
                                    )
                                )
    price = forms.DecimalField(initial=10000)
    summary = forms.CharField(required=False, widget=forms.Textarea)