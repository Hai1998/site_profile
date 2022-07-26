from django.shortcuts import loader
from django.template import Template, loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Commercials


# Create your views here.
def homeSetting(request):
    commercials = Commercials.objects.all().values()
    template = loader.get_template('settings/viewCommercial.html')
    context = {
        'title': 'view',
        'commercials': commercials
    }
    return HttpResponse(template.render(context, request))


def addCommercial(request):
    template = loader.get_template('settings/addCommercial.html')
    return HttpResponse(template.render({}, request))
