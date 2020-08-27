from django.forms import ModelForm
from store.models import Picture


class PictureForm(ModelForm):
    class Meta:
        model = Picture
        exclude = ['id', 'upload_time']
