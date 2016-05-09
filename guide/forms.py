from django import forms

class CodeForm(forms.Form):
    code = forms.IntegerField(label='Object Code')
