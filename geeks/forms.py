from django import forms
from . import models


class GeeksForm(forms.ModelForm):

    class Meta:

        model = models.GeeksModel
        fields = [
            'title',
            'description'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }
