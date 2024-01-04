from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, DetailView

from manae_users_demos.auth_app.forms import RegisterForm, LoginForm
from manae_users_demos.auth_app.models import ToDo


# password = 1234QWer!

class HomePage(TemplateView):
    template_name = 'home.html'


class RegisterUserView(CreateView):
    template_name = 'register.html'
    form_class = RegisterForm

    success_url = reverse_lazy('login')


class LoginViewTemplate(LoginView):
    template_name = 'login.html'
    form_class = LoginForm

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)


class LogoutViewTemplate(View):

    @staticmethod
    def get(request):
        logout(request)
        return redirect(reverse_lazy('home'))


@method_decorator(login_required(login_url='login'), name='dispatch')
class UserToDoList(ListView):
    model = ToDo
    template_name = 'to_do.html'
    paginate_by = 4

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator(login_required(login_url='login'), name='dispatch')
class ToDoCreateView(LoginRequiredMixin, CreateView):
    model = ToDo
    fields = ['title', 'description']
    template_name = 'to_do_create.html'
    success_url = reverse_lazy('to_do')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ToDoDelete(DeleteView):
    model = ToDo
    template_name = 'to_do.html'
    success_url = reverse_lazy('to_do')


@method_decorator(login_required(login_url='login'), name='dispatch')
class MyAccount(LoginRequiredMixin, DetailView):
    template_name = 'account.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        articles_count = ToDo.objects.filter(author=user).count()
        context['articles_count'] = articles_count
        return context

