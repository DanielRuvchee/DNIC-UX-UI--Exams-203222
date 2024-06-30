from django import forms
from .models import Suplement

class SuplementForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SuplementForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Suplement
        exclude = ('user',)