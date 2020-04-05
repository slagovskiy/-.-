from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def pool_edit(request, uuid):
    if request.user.is_anonymous:
        return redirect('/')
    pool = None
    if uuid != '0':
        pool = Pool.objects.get(uuid=uuid)
        if pool.user.username != request.user.username:
            return redirect(reverse('account_profile'))
    if request.method == 'GET':
        content = {
            'pool': pool
        }
        return render(request, 'pool_edit.html', content)
    elif request.method == 'POST':
        data = request.POST
        print (data)
        return JsonResponse({ 'data': 'ok' })
        '''
        if 'username' in request.POST:
            request.user.first_name = request.POST.get('username', '')
            user = User.objects.get(id=request.user.id)
            user.first_name = request.POST.get('username', '')
            user.save()
            return redirect('/accounts/profile/')
        '''


def pool_view(request, uuid):
    pool = None
    if uuid != '0':
        pool = Pool.objects.get(uuid=uuid)
    if request.method == 'GET':
        content = {
            'pool': pool
        }
        return render(request, 'pool_view.html', content)
    elif request.method == 'POST':
        pass
        '''
        if 'username' in request.POST:
            request.user.first_name = request.POST.get('username', '')
            user = User.objects.get(id=request.user.id)
            user.first_name = request.POST.get('username', '')
            user.save()
            return redirect('/accounts/profile/')
        '''


