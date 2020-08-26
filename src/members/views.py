from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SighnUpForm,EditProfileForm,PasswordChangingForm,ProfilePageForm
from django.views.generic import DeleteView,CreateView
from theblog.models import Profile




class CreateProfilePageView(CreateView):
    model = Profile
    template_name = 'registration/create_profile_page.html'
    form_class  = ProfilePageForm

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super ().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    # fields = ['bio','profile_pic','Profile_Cover','website_url',
    # 'facebook_url','twtter_url','instgram_url','phone',
    # 'country','Gender','address','Profile_Cover','Favorite',]
    success_url = reverse_lazy('home')
    form_class  = ProfilePageForm


def password_success(request):
    return render(request, 'registration/password_success.html', {})


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    #form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')



class UserRegisterView(generic.CreateView):
    form_class = SighnUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')



class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class UserProfile(DeleteView):
    model = Profile
    template_name = 'registration/profile.html'
    # success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        
        context = super(UserProfile,self).get_context_data()
        Page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        
        context['Page_user'] = Page_user
        return context