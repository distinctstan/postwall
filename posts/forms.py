from django import forms
from .models import Post,Category,Comment

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Type Content'}))
    thumbnail = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control','placeholder':'Thumbnail Image'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select(attrs={'class':'form-select','placeholder':'Category'}))

    class Meta:
        model = Post
        fields = ['title','content','thumbnail','category']


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control w-100','cols':'30','rows':'5','placeholder':'Type your comment here'}))
    class Meta:
        model = Comment
        fields = ['content']