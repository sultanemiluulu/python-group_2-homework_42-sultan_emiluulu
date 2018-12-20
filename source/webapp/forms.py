from django import forms

class SearchArticleForm(forms.Form):
    article_name = forms.CharField(max_length=50, required=False, label='Article')
