from django.forms import ModelForm
from .models import Target

class TargetForm(ModelForm):
    class Meta:
        model = Target
        fields = ['target_name']
        #target_name = forms.CharField(label="Your target", max_length=100)
