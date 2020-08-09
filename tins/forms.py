from django import forms

from .models import Tins


MAX_TIN_LENGTH = 300
class TinsForm(forms.ModelForm):
    class Meta:
        model = Tins
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TIN_LENGTH:
            raise forms.ValidationError("Reduce the size of your tin")
        if content == "":
            raise forms.ValidationError("Add some-tin")
        return content 