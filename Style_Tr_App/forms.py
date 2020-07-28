from django import forms
from .models import Style_Tr


class ImageForm(forms.ModelForm):
    class Meta:
        model = Style_Tr
        fields = ('img_content', 'img_style')
