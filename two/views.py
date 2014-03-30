# Create your views here.
#from django.http import HttpResponse

#def index(request):
    #return HttpResponse("Hello, world. You're at the index page.")
    
    
    
from django.http import HttpResponse
from django.template import RequestContext, loader

from two.models import Position

def index(request):
    latest_position_list = Position.objects.order_by('pub_date')
    template = loader.get_template('two/index.html')
    context = RequestContext(request, {
        'latest_poll_list': latest_position_list,
    })
    return HttpResponse(template.render(context))    
    
    
