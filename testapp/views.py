from django.shortcuts import render, redirect
from .models import News, NewsCategory, Favorite
from .forms import RegForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views import View

def home_page(request):
    news = News.objects.all()
    categories = NewsCategory.objects.all()
    context = {'news': news, 'categories': categories}
    return render(request, 'home.html', context)

def category_page(request, pk):
    category = NewsCategory.objects.get(id=pk)
    news = News.objects.filter(news_category=category)
    context = {'category': category, 'news': news}
    return render(request, 'category.html', context)

def news_page(request, pk):
    news = News.objects.get(id=pk)
    context = {'news': news}
    return render(request, 'news.html', context)

def about_page(request):
    return render(request, 'about.html')

def contacts_page(request):
    return render(request, 'contacts.html')

class Register(View):
    template_name = 'register.html'

    def get(self, request):
        form = RegForm()  # Создаем пустую форму
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RegForm(request.POST)  # Здесь мы используем вашу форму

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            user = User.objects.create_user(username=username, email=email, password=password).save()
            login(request, user)
            return redirect('/')  # Перенаправляем на главную страницу

        return render(request, self.template_name, {'form': form})  # Отправка обратно с ошибками

def logout_view(request):
    logout(request)
    return redirect('/')

def to_favorite(request, pk):
    if request.method == 'POST':
        news = News.objects.get(id=pk)
        Favorite.objects.create(user_id=request.id, user_news=news).save()
        return redirect('/')

def del_from_favorite(request, pk):
    news_to_del = News.objects.get(id=pk)
    Favorite.objects.filter(user_news=news_to_del).delete()

    return redirect('/favorite')

def favorite(request):
    user_favorite = Favorite.objects.filter(user_id=request.id)
    news_ids = [n.user_news.id for n in user_favorite]

