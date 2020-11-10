from django import forms
from .models import Product


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'image',
            'media',
        ]
        exclude = [
            'price'
        ]

    def cleaned_content(self):
        data = self.cleaned_data.get('content')
        if len(data) < 4:
            raise forms.ValidationError('This is not long enough.')
        return data
