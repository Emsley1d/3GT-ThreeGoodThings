from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import DetailView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def help(request):
    return render(request, 'help.html')

def profile(request):
    return render(request, 'profile.html')


# USER

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# class PasswordChange(generic.CreateView):
#     form_class = UserCreationForm
#     # !still redirects to change_done
#     success_url = reverse_lazy('home')
#     template_name = "registration/password_change_form.html"

#     def form_valid(self, form,):
#         response = super().form_valid(form)
#         # !doesnt work yet.
#         messages.success(self.request, 'Your password has been changed successfully.')
#         return redirect('home')
    
    # def get_success_url(self):
    #     return self.success_url

class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy('user/detail.html')
    template_name = "registration/password_change_form.html"

    def form_valid(self, form):
        messages.success(self.request, 'Your password has been changed successfully.')
        return super().form_valid(form)
    
class CustomPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('detail')
    success_message = "Your password has been changed successfully."

class PasswordReset(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/password_reset.html"

class UserDetail(LoginRequiredMixin, DetailView):
    model = User
    template_name='user/detail.html' 

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    template_name='user/update.html'
    fields = '__all__'

class UserDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = User
    template_name='user/user_confirm_delete.html'
    success_url = '/'
    success_message = "Your 3GT account has been deleted."
    
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful. Please log in to continue.')
            return redirect('home')
    else:
        form = UserRegistrationForm()
        messages.error(request, 'Registration unsuccessful, please try again.')

        all_messages = messages.get_messages(request)
        for message in all_messages:
            message.used = True


    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Register'))
    form.helper = helper
    
    return render(request, 'registration/register.html', {'form': form})