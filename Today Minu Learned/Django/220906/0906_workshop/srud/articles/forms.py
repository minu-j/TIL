from turtle import textinput
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목을 입력해주세요',
                'maxlength': 10,
            }
        ),
    )
    content = forms.CharField(
        label = '내용',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '내용을 입력해주세요',
            }
        )
    )
    class Meta:
        model = Article
        fields = '__all__'