from django import forms
from CRUDOperation.models import ChimModel

class chimforms(forms.ModelForm):
    class Meta:
        model= ChimModel
        fields= "__all__"
