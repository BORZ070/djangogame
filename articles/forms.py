from django import forms
from articles.models import Article



class ArticleEditForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['text']

