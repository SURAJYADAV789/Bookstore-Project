from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        
        fields='__all__'
        widgets={
            'book_name':forms.TextInput(attrs={'class':'form-control '}),
            'book_price':forms.NumberInput(attrs={'class':'form-control'}),
            'book_desc':forms.Textarea(attrs={'class':'form-control'})
            
        }