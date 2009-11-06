from django import forms
from django.utils.text import get_text_list, capfirst

from lingo.models import LabelCustomization

class LingoForm(forms.ModelForm):
    def __init__(self, user=None):
        super(LingoForm, self).__init__()
        if user:
            labels = LabelCustomization.objects.filter(user=user, app_label=self._meta.model._meta.app_label, model_name=self._meta.model.__name__)
            for label in labels:
                self.fields[label.field].label = label.custom_label
                pass
