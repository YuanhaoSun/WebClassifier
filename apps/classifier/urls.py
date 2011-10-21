from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns("",
    url(r"^$", 'classifier.views.home', name='home'),
    url(r"^classify/", 'classifier.views.classify', name='classify'),
)
