from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from theblog.models import Profile,Gender,Favorite_chose

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','profile_pic','Profile_Cover','website_url',
        'facebook_url','twtter_url','instgram_url','phone','address',
        'country','Gender','Favorite')
        widgets = {
            'bio' : forms.Textarea(attrs={'class' : 'form-control bg-transparent text-light','style' : "height: 135px; "}),
            'website_url' : forms.TextInput(attrs={'class' : 'form-control bg-transparent text-light'}),
            'facebook_url' : forms.TextInput(attrs={'class' : 'form-control bg-transparent text-light'}),
            'twtter_url' : forms.TextInput(attrs={'class' : 'form-control bg-transparent text-light'}),
            'instgram_url' : forms.TextInput(attrs={'class' : 'form-control bg-transparent text-light'}),
            'phone' : forms.TextInput(attrs={'class' : 'form-control bg-transparent text-light'}),
            'Gender' : forms.Select(choices=Gender,attrs={'class' : 'custom-select mr-sm-2 bg-dark text-light'}),
            'country' : forms.Select(attrs={'class' : 'custom-select mr-sm-2 bg-dark text-light'}),
            'Favorite' : forms.Select(choices=Favorite_chose,attrs={'class' : 'form-control bg-dark text-light'}),
            'address' : forms.TextInput(attrs={'class' : 'form-control bg-transparent text-light'}),
            #'profile_pic' : forms.Select(attrs={'class' : 'custom-select mr-sm-2'}),
            #'Profile_Cover' : forms.Select(choices=choice_list,attrs={'class' : 'custom-select mr-sm-2'}),
        }





class SighnUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control bg-transparent text-light'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control bg-transparent text-light'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control bg-transparent text-light'}))
    

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')


    def __init__(self,*args, **kwargs):
        super(SighnUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control bg-transparent text-light'
        self.fields['password1'].widget.attrs['class'] = 'form-control bg-transparent text-light'
        self.fields['password2'].widget.attrs['class'] = 'form-control bg-transparent text-light'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control bg-transparent text-light'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control bg-transparent text-light'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control bg-transparent text-light'}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control bg-transparent text-light'}))
    #last_login = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    #is_superuser = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class' : 'form-check'}))
    #is_staff = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class' : 'form-check'}))
    #is_active = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class' : 'form-check'}))
    date_joined = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control bg-transparent text-light'}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','date_joined')





class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control bg-transparent text-light', 'type' : 'password'}))
    new_password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class' : 'form-control bg-transparent text-light', 'type' : 'password'}))
    new_password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class' : 'form-control bg-transparent text-light', 'type' : 'password'}))
    

    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')



