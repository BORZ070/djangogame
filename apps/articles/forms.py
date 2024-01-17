from django import forms
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget

from articles.models import Article

class ArticleEditForm(forms.ModelForm):

    text = SummernoteTextField()

    class Meta:
        model = Article
        fields = ['text']
        widgets = {
            'text': SummernoteWidget(),
        }


