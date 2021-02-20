from .models import Product
from django.forms import ModelForm, TextInput, Textarea


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["title", "opisanie"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "opisanie": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
        }