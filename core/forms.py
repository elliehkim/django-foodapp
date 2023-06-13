from django import forms

# Create your forms here.

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter your name',
        'class': 'contact-input'
    }), max_length = 100)

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder' : 'Enter your email address',
        'class': 'contact-input'
    }), max_length = 200)

    subject = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter your subject',
        'class': 'contact-input'
    }), max_length = 200)

    message = forms.CharField(widget = forms.Textarea(attrs={
        'placeholder' : 'Enter your message',
        'class': 'contact-input'
    }), max_length = 2000)
