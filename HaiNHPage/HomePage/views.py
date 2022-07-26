from django.http import HttpResponse
from django.template import loader
# Create your views here.


def home(request):
    template = loader.get_template('homepage/index.html')
    return HttpResponse(template.render())
