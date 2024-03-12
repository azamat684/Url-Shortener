from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import string
import random
from django.shortcuts import render, redirect
from .models import URL

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(characters, k=6))
    return short_url
@csrf_exempt
def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST['long_url']
        short_url = generate_short_url()
        URL.objects.create(long_url=long_url, short_url=short_url)
        return render(request, 'main/shortened.html', {'short_url': short_url})
    return render(request, 'index.html')