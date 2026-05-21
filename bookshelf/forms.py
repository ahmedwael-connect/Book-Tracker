from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # Expose these fields in the HTML Form
        fields = ['title', 'author', 'status', 'rating']

        # Optional: Add custom styling classes to the form inputs
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter author name'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'rating': forms.NumberInput(
                attrs={'class': 'form-input', 'min': 1, 'max': 5, 'placeholder': 'Rating (1-5, Optional)'}),
        }