#log/forms.py
from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from .models import Comment, CommentPhoto

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content')
        widgets = {
            'content' : forms.Textarea(attrs={
                'rows': '4',
                'cols': '32',
                'maxlength': '500',
            }),
        }

class CommentPhotoForm(forms.ModelForm):
	content = forms.CharField(label ="", widget = forms.Textarea(
	attrs ={
		'class':'form-control',
		'placeholder':'Comment here !',
		'rows':4,
		'cols':50
	}))
	class Meta:
		model = CommentPhoto
		fields =['content']

