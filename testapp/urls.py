from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('about', views.about_page),
    path('contacts', views.contacts_page),
    path('register', views.Register.as_view()),
    path('category/<int:pk>', views.category_page),
    path('news/<int:pk>', views.news_page),
    path('add-to-favorite/<int:pk>', views.to_favorite),
    path('del-from-favorite/<int:pk>', views.del_from_favorite),
    path('favorite', views.favorite),
    path('logout', views.logout_view)
]