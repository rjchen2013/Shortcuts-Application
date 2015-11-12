from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from . import views
from .views import IndexView, ShortcutFormView

urlpatterns = patterns('',
                       url(r'^$',
                           IndexView.as_view(),
                           name='index'),
                       url(r'form/$',
                           ShortcutFormView.as_view(template_name='shortcuts/detail.html'),
                           name='form'),
)