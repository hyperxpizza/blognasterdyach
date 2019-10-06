from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=40)
    email = forms.EmailField()
    body = forms.CharField(required=False,widget=forms.Textarea)