from django import forms

class TargetForm(forms.Form):
    target_name = forms.CharField(label="Your target", max_length=100)
