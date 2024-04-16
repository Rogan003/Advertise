from django.forms import ModelForm
from .models import Ad

class PostForm(ModelForm):
    class Meta:
        model = Ad
        exclude = ['likes', 'dislikes', 'user']