from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def profile(request):
    if request.user.is_anonymous:
        return redirect('/')
    if request.method == 'GET':
        content = {
        }
        return render(request, 'profile.html', content)
    elif request.method == 'POST':
        if 'username' in request.POST:
            request.user.first_name = request.POST.get('username', '')
            user = User.objects.get(id=request.user.id)
            user.first_name = request.POST.get('username', '')
            user.save()
            return redirect('/accounts/profile/')


