from django import forms
from . models import book,Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = '__all__'

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the Book name'}),
            'author':forms.Select(attrs={'class':'form-control','placeholder':'Enter the Book Author name'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the Book Price'}),
        }