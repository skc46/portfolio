from django import forms

from .models import ContactForm

class MessageForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields=['Name', 'Email', 'Message']

# class ContactForm1(forms.Form):
#     subject = forms.CharField(max_length=100)
#     email = forms.EmailField(required=False)
#     message = forms.CharField(widget=forms.Textarea)