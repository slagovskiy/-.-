from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .pools.models import Pool


def profile(request):
    if request.user.is_anonymous:
        return redirect('/')
    pools = Pool.objects.all().filter(user=request.user)
    if request.method == 'GET':
        content = {
            'pools': pools
        }
        return render(request, 'profile.html', content)
    elif request.method == 'POST':
        if 'username' in request.POST:
            request.user.first_name = request.POST.get('username', '')
            user = User.objects.get(id=request.user.id)
            user.first_name = request.POST.get('username', '')
            user.save()
            return redirect('/accounts/profile/')


