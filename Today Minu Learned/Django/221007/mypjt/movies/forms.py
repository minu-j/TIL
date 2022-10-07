from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Input Title', 'type':'text'}),
            'audience': forms.NumberInput(
                attrs={'class':'form-control', 'placeholder':'Input Audience', 'type':'number'}),
            'release_date': forms.DateInput(
                format=('%Y-%m-%d'), 
                attrs={'class':'form-control', 'type':'date'}),
            'genre': forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Input Genre', 'type':'text'}),
            'score': forms.NumberInput(
                attrs={'class':'form-control', 'placeholder':'Input Score', 'type':'number', 'min': "0", 'max': "5", 'step': "0.5"}),
            'poster_url': forms.TextInput(
                attrs={'class':'form-control', 'placeholder':'Input Poster URL', 'type':'url'}),
            'description': forms.Textarea(
                attrs={'class':'form-control', 'placeholder':'Input Description', 'type':'textarea'}),
        }