from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # The PostForm will be the name of the form, passing in a ModelForm so that Django knows what to use

    class Meta:
        # Tells what model to use for the form, we also specify what fields should show up in the form
        model = Post
        fields = ('title', 'text')
