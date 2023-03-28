from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import DetailView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib import messages


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def help(request):
    return render(request, 'help.html')

def profile(request):
    return render(request, 'profile.html')

def stats(request):
    return render(request, 'stats.html')


# USER

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class PasswordChange(generic.CreateView):
    form_class = UserCreationForm
    # still redirects to change_done
    success_url = '/'
    template_name = "registration/password_change_form.html"

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     # doesnt work yet.
    #     messages.success(self.request, 'Your password has been changed successfully.')
    #     return response

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

class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    success_url = '/'
    template_name='user/user_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        # doesnt work yet.
        # messages.success(request, 'Account successfully deleted.')
        return super().delete(request, *args, **kwargs)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Registration successful. Please log in to continue.')
            return redirect('home')
    else:
        form = UserRegistrationForm()
        # messages.error(request, 'Registration unsuccessful, please try again.')

        # all_messages = messages.get_messages(request)
        # for message in all_messages:
        #     message.used = True


    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Register'))
    form.helper = helper
    
    return render(request, 'registration/register.html', {'form': form})