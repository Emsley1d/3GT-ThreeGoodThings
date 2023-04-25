from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.forms import PasswordResetForm
from django.views.generic import DetailView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
import secrets
from main_app.models import EmailVerification
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings



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

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             messages.success(request, 'Registration successful. Please log in to continue.')
#             return redirect('home')
#     else:
#         form = UserRegistrationForm()
#         messages.error(request, 'Registration unsuccessful, please try again.')

#         all_messages = messages.get_messages(request)
#         for message in all_messages:
#             message.used = True


#     helper = FormHelper()
#     helper.form_method = 'POST'
#     helper.add_input(Submit('submit', 'Register'))
#     form.helper = helper
    
#     return render(request, 'registration/register.html', {'form': form})

# #! AWS EMAIL VERIFICATION
# # Generate a random verification code
# verification_code = secrets.token_urlsafe(32)

# # Create a new record in the EmailVerification model
# EmailVerification.objects.create(email=email, verification_code=verification_code)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Create user object
            user = form.save()
            # Generate verification code
            verification_code = secrets.token_urlsafe(20)
            # Create EmailVerification object
            EmailVerification.objects.create(email=user.email, verification_code=verification_code)
            # Send verification email to user
            send_verification_email(user.email, verification_code)
            messages.success(request, 'Registration successful. Please check your email to verify your account.')
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

def send_verification_email(email, verification_code):
    subject = 'Please Verify Your Email Address'
    message = f'Hi, please click on the following link to verify your email address: {settings.BASE_URL}/verify-email/{verification_code}/'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)

class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'

    def get_success_url(self):
        return reverse_lazy('detail', args=[self.request.user.pk])
    
    
class PasswordChange(PasswordChangeView):
    template_name = 'registration/password_change_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.success_url = reverse_lazy('detail', args=[request.user.pk])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Your password has been changed successfully.')
        return super().form_valid(form)
    
class CustomPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_message = "Your password has been changed successfully."

    def get_success_url(self):
        return reverse_lazy('detail', args=[self.request.user.pk])

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return redirect(self.get_success_url())

class PasswordReset(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/password_reset.html"

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "3GoodThings/main_app/templates/registration/password_reset_email.html"
					c = {
					"email": user.email,
					'domain': '127.0.0.1:8000',
					'site_name': '3GT',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, '3gtproject@gmail.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="3GoodThings/main_app/templates/registration/password_reset_email.html", context={"password_reset_form":password_reset_form})

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
    
