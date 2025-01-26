from django.shortcuts import render, redirect
from .models import News, NewsCategory
from .forms import RegForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views import View

# Create your views here.
def home_page(request):
    return render(request, 'home.html')


def about_page(request):
    return render(request, 'about.html')


def contacts_page(request):
    return render(request, 'contacts.html')

class Register(View):
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name)


    def post(self, request):
        form = request.POST

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password).save()
            login(request, user)
            return redirect('/')



