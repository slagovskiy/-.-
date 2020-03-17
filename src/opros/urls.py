from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.views.generic.base import TemplateView
from .views import profile, pool_edit


admin.autodiscover()


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('policy/', TemplateView.as_view(template_name='policy.html')),
    path('receiver/', TemplateView.as_view(template_name='receiver.html')),
    path('accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', profile, name='account_profile'),
    url(r'^pool/edit/$', pool_edit, name='pool_edit'),
    path('admin/', admin.site.urls),
]
