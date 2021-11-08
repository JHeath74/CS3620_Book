from django import forms
from .models import BookData


class Add_New_Book_Form(forms.ModelForm):
    class Meta:
        model = BookData
        fields = ['Book_Name', 'Book_Category', 'Book_ISBN', 'Book_Description', 'Book_Rating', 'Book_Image']
