from django import forms
from .models import Vote

class VoteForm(forms.ModelForm):

    class Meta:
        model = Vote
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': '제목을 입력하세요',
                }
            ),
            'issue_a': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'issue_b': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            )
        }
