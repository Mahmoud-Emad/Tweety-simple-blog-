from django import forms
from .models import Post,category,Comment

choices = category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append (item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title' , 'title_tag', 'auther' , 'category' , 'body' ,'header_image')

        widgets = {

            'title' : forms.TextInput(attrs={'class' : 'form-control bg-transparent text-light'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control bg-transparent text-light'}),
            'auther' : forms.TextInput(attrs={'class' : 'form-control bg-transparent text-light ','value':'' ,'id':'bob', 'type':'hidden'}),
            #'auther' : forms.Select(attrs={'class' : 'custom-select mr-sm-2'}),
            'category' : forms.Select(choices=choice_list,attrs={'class' : 'custom-select mr-sm-2 bg-dark text-light'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control bg-transparent'}),

            
        

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title' , 'title_tag', 'category', 'body')

        widgets = {

            'title' : forms.TextInput(attrs={'class' : 'form-control bg-transparent'}),
            'title_tag' : forms.TextInput(attrs={'class' : 'form-control bg-transparent'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control bg-transparent'}),
            'category' : forms.Select(choices=choice_list,attrs={'class' : 'custom-select mr-sm-2'}),
        

        }


class CatForm(forms.ModelForm):
    class Meta:
        model = category
        fields = '__all__'

        widgets = {

            'name' : forms.TextInput(attrs={'class' : 'form-control'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name' , 'body')

        widgets = {

            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),        
        }
