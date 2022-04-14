from django import forms
from .models import Posts , Category

choices = Category.objects.all().values_list('name','name')
choices_list = []
for items in choices:
    choices_list.append(items)
#choices = [('coding','coding'),('sports','sports'),('entertainment','entertainment')]

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('author','title','photo', 'category','content')
        widgets = {
            #'author': forms.Select(attrs= {'class': 'form-control'}),
            'author': forms.TextInput(attrs= {'class': 'form-control','value': '', 'id': 'elder', 'type':'hidden'}),
            'category': forms.Select(choices = choices_list , attrs= {'class': 'form-control'}),
            'title': forms.TextInput(attrs= {'class': 'form-control'}),
            #'Photo': forms.ImageField(attrs= {'class': 'form-control'}),
            'content': forms.Textarea(attrs= {'class': 'form-control'}),
        }   

class EditForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title','photo', 'category','content')
        widgets = {
            'author': forms.Select(attrs= {'class': 'form-control'}),
            'category': forms.Select(choices = choices_list , attrs= {'class': 'form-control'}),
            'title': forms.TextInput(attrs= {'class': 'form-control'}),
            #'Photo': forms.ImageField(attrs= {'class': 'form-control'}),
            'content': forms.Textarea(attrs= {'class': 'form-control'}),
        }   