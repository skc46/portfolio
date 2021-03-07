from django import forms

from .models import ContactForm

class MessageForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields=['Name', 'Email', 'Message']

        widgets = {
            'Name': forms.TextInput(attrs ={'class': 'form-label'}),
            'Email': forms.EmailInput(attrs ={'class': 'form-label'}),
            'Message': forms.Textarea(attrs ={'class': 'form-label'}),
        }

        

# class ContactForm1(forms.Form):
#     subject = forms.CharField(max_length=100)
#     email = forms.EmailField(required=False)
#     message = forms.CharField(widget=forms.Textarea)