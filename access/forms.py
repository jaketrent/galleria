from django import forms

class CreateAccessTokenForm(forms.Form):
    collection_id = forms.IntegerField(widget=forms.HiddenInput(), required=True)

