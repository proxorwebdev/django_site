from django import forms

class GuestbookForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
