from django import forms
from webapp.models import Article, Comment

class SearchArticleForm(forms.Form):
    article_name = forms.CharField(max_length=50, required=False, label='Article')


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['headline', 'author', 'text']


class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['headline', 'author', 'text']


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', 'author', 'article']


class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

