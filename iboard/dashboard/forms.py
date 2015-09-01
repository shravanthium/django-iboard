from django import forms

class IssueForm(forms.Form):
    url = forms.CharField()
