# products 글 작성 ModelForm 생성

from django import forms


class ProductForm(forms.Form):
    title = forms.CharField(max_length=100)
    price = forms.IntegerField()
    content = forms.TextField()