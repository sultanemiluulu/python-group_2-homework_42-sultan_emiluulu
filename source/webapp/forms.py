from django import forms
from webapp.models import Article

class SearchArticleForm(forms.Form):
    article_name = forms.CharField(max_length=50, required=False, label='Article')


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['headline', 'author', 'text']


