from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ShortenedURL, ShortURLList
from .forms import ShortenURLForm
import random
import string

from django.core.paginator import Paginator


def generate_slug():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def shorten_url(request):
    if request.method == 'POST':
        form = ShortenURLForm(request.POST)
        if form.is_valid():
            long_url = form.cleaned_data['long_url']
            slug = form.cleaned_data['slug']
            if not slug:
                slug = generate_slug()
            ShortenedURL.objects.create(long_url=long_url, slug=slug)
            return render(request, 'shortened_url.html', {'shortened_url': slug})
    else:
        form = ShortenURLForm()
    return render(request, 'shorten_url.html', {'form': form})

def redirect_to_long_url(request, slug):
    shortened_url = get_object_or_404(ShortenedURL, slug=slug)
    return redirect(shortened_url.long_url)


#yaratilgan qisqa urllar ro'yxati
def short_url_list(request):
    short_urls = ShortURLList.objects.all().select_related('shortened_url')
    paginator = Paginator(short_urls, 10)  # 10 qisqa URL ni bir page da chiqarish
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'short_url_list.html', {'page_obj': page_obj})
