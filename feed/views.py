from django.shortcuts import render,redirect
from django.forms.models import BaseModelForm
from django.shortcuts import render,get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.

from .forms import PositionForm


class CustomLoginView(LoginView):
    template_name = 'feed/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('feed')


class RegisterPage(FormView):
    template_name = 'feed/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('feed')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('feed')
        return super(RegisterPage, self).get(*args, **kwargs)


def home(request):
    return render(request,'feed/feed.html')
