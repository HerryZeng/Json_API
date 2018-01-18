from django.urls import path,re_path
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views1
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='example/index.html')),
    # re_path('ajax/more/', view=views1.more_poems),
    url(r'ajax/more/$', view=views.more_poems),
    url(r'ajax/add/$', view=views.add),
]
