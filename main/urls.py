from django.urls import path
from . import views


urlpatterns = [
    path('', views.shorten_url, name='shorten_url'),
    path('short-url-list/', views.short_url_list),
    path('<slug:slug>/', views.redirect_to_long_url, name='shortened_url_detail')
]