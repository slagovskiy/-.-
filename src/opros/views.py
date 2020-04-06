import json
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .pools.models import Pool, Question, Answer, UserAnswer


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
        data = json.loads(request.POST.get('pool', '-1'))
        if data != '-1':
            pool = None
            if data['uuid'] == '':
                pool = Pool.objects.create(
                    user = request.user,
                    title = '',
                )
            else:
                pool = Pool.objects.get(uuid=data['uuid'])
            pool.title = data['title']
            pool.password = data['password']
            pool.limit = int(data['limit'])
            pool.comments = data['comments']
            pool.save()

            for q in data['questions']:
                question = None
                if q['uuid'] == '':
                    question = Question.objects.create(
                        pool = pool,
                        title = '',
                        order = 0
                    )
                else:
                    question = Question.objects.get(uuid=q['uuid'])
                question.title = q['title']
                question.order = int(q['order'])
                question.deleted = q['deleted']
                question.save()

                for a in q['answers']:
                    answer = None
                    if a['uuid'] == '':
                        answer = Answer.objects.create(
                            question = question,
                            title = ''
                        )
                    else:
                        answer = Answer.objects.get(uuid=a['uuid'])
                    answer.question = question
                    answer.title = a['title']
                    answer.link = a['link']
                    answer.deleted = a['deleted']
                    answer.save()

        return JsonResponse({ 'data': 'ok' })
        '''
        {
            'uuid': '', 
            'title': 'pool_title', 
            'password': '', 
            'limit': 0, 
            'comments': True, 
            'questions': [
                {
                    'uuid': '', 
                    'title': 'Question_title_1', 
                    'order': 0, 
                    'deleted': False, 
                    'answers': [
                        {
                            'uuid': '', 
                            'title': 'answer_1', 
                            'link': '', 
                            'show_link': False, 
                            'deleted': False
                        }, 
                        {
                            'uuid': '', 
                            'title': 'answer_2', 
                            'link': '', 
                            'show_link': False, 
                            'deleted': False
                        }
                    ]
                }, 
                {
                    'uuid': '', 
                    'title': 'Questuion_title_2', 
                    'order': 0, 
                    'deleted': False, 
                    'answers': [
                        {
                            'uuid': '', 
                            'title': 'answer_1', 
                            'link': '', 
                            'show_link': False, 
                            'deleted': False
                        }, 
                        {
                            'uuid': '', 
                            'title': 'answer_2', 
                            'link': '', 
                            'show_link': False, 
                            'deleted': False
                        }, 
                        {
                            'uuid': '', 
                            'title': 'answer_3', 
                            'link': '', 
                            'show_link': False, 
                            'deleted': False
                        }
                    ]
                }
            ]
        }
        '''


@csrf_exempt
def pool_view(request, uuid):
    pool = None
    ua = []
    if uuid != '0':
        pool = Pool.objects.get(uuid=uuid)
        for q in pool.question_set.all().filter(deleted=False):
            ua.append(UserAnswer.objects.all().filter(
                question=q,
                useragent=request.META['HTTP_USER_AGENT'] + ' ' + request.META['REMOTE_HOST'],
                ipaddress=request.META['REMOTE_ADDR']
            ).last())
    if request.method == 'GET':
        content = {
            'pool': pool,
            'ua': ua
        }
        return render(request, 'pool_view.html', content)
    elif request.method == 'POST':
        data = json.loads(request.POST.get('answer', '-1'))
        if data != '-1':
            for k,v in data.items():
                ua = UserAnswer.objects.all().filter(
                    question = Question.objects.get(uuid=k),
                    #answer = Answer.objects.get(uuid=v),
                    useragent = request.META['HTTP_USER_AGENT'] + ' ' + request.META['REMOTE_HOST'],
                    ipaddress = request.META['REMOTE_ADDR']
                ).last()
                if ua:
                    ua.answer = Answer.objects.get(uuid=v)
                    ua.save()
                else:
                    ua = UserAnswer.objects.create(
                        question=Question.objects.get(uuid=k),
                        answer=Answer.objects.get(uuid=v),
                        useragent=request.META['HTTP_USER_AGENT'] + ' ' + request.META['REMOTE_HOST'],
                        ipaddress=request.META['REMOTE_ADDR']
                    )
                    ua.save()
        return JsonResponse({ 'data': 'ok' })


def pool_stat(request, uuid):
    pool = None
    if uuid != '0':
        pool = Pool.objects.get(uuid=uuid)
    if request.method == 'GET':
        content = {
            'pool': pool
        }
        return render(request, 'pool_stat.html', content)
    elif request.method == 'POST':
        return JsonResponse({ 'data': 'ok' })

