from django.shortcuts import loader
from django.template import Template, loader
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from .models import Commercials
from django.urls import reverse
import os



# Create your views here.
def homeSetting(request):
    commercials = Commercials.objects.all().values()
    template = loader.get_template('settings/homeSetting.html')
    context = {
        'title': 'view',
        'commercials': commercials
    }
    return HttpResponse(template.render(context, request))


def addCommercial(request):
    template = loader.get_template('settings/homeSetting.html')
    return HttpResponse(template.render({}, request))


def addRecordCommercial(request):
    data = request.POST.getlist('commercial')
    image = request.FILES.get('file_image')
    fss = FileSystemStorage()
    file = fss.save(image.name, image)
    file_url = fss.url(file)
    commercial = Commercials(first_text=data[0], second_text=data[1], thirst_text=data[2], image_name=image.name, commercials_image=file_url)
    commercial.save()
    return HttpResponseRedirect(reverse('settings'))


def updateCommercial(request, id):
    commercial = Commercials.objects.get(id=id)
    template = loader.get_template('settings/homeSetting.html')
    context = {
        'title': 'update',
        'commercial': commercial
    }
    return HttpResponse(template.render(context, request))


def updateRecordCommercial(request, id):
    data = request.POST.getlist('commercial')
    image = request.FILES.get('file_image')
    fss = FileSystemStorage()
    file = fss.save( image.name, image )
    file_url = fss.url(file)
    commercial = Commercials.objects.get(id=id)
    commercial.first_text = data[0]
    commercial.second_text = data[1]
    commercial.thirst_text = data[2]
    commercial.image_name = image.name
    commercial.commercials_image = file_url
    commercial.save()
    return HttpResponseRedirect(reverse('settings'))


def deleteCommercial(request, id):
    commercial = Commercials.objects.get(id=id)
    image_url = commercial.commercials_image
    commercial.delete()
    # os.remove(image_url)
    return HttpResponseRedirect(reverse('settings'))
