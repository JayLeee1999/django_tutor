from django.forms import ModelForm
from community.models import Article


class Form(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'name', 'contents', 'url', 'email']
