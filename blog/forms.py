from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    email = forms.EmailField()
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'post': forms.HiddenInput(),
            'active': forms.HiddenInput()
        }

class SearchForm(forms.Form):
    query = forms.CharField(max_length = 100)
