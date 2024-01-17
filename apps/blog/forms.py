from django import forms
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget

from blog.models import Blog

class BlogEditForm(forms.ModelForm):

    text = SummernoteTextField()

    class Meta:
        model = Blog
        fields = ['text']
        widgets = {
            'text': SummernoteWidget(),
        }
