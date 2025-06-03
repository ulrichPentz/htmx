from django import forms
from .models import Products

class ItemForm(forms.ModelForm):
        class Meta:
            model = Products
            fields = ['app_name', 'app_email']