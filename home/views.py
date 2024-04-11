from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseNotFound
from django.conf import settings

import os

# Create your views here.

def path(request, path):
    template_path = 'home/site_content/' + path
    template_exist = os.path.normpath(settings.BASE_DIR / 'home/templates/' / template_path)

    if os.path.exists(template_exist):
        return TemplateView.as_view(template_name=template_path)(request)
    else:
        return HttpResponseNotFound(TemplateView.as_view(template_name='home/404.html')(request).render())