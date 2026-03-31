from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.views.generic.edit import CreateView
from .models import Account, City
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.http import HttpResponseRedirect

# Create your views here.


class LoginView(DjangoLoginView):
    template_name = 'users/login.html'


class RegisterView(CreateView):
    template_name = 'users/register.html'
    model = Account
    context_object_name = 'form'
    fields = ['email', 'first_name', 'last_name', 'password']
    success_url = reverse_lazy('pages:home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        city = City.objects.get(name=form.cleaned_data['city'])
        user.city = city
        user.save()

        login(self.request, user)
        self.object = user

        return HttpResponseRedirect(self.get_success_url())


class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy('users:login')
