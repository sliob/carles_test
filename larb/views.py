from django.shortcuts import render_to_response, render
from django.template import RequestContext
import os

# Create your views here.


def index(request):
    return render_to_response("larb/index.html", context_instance=RequestContext(request))
    #return render_to_response("larb/index.html", RequestContext(request))
    # return render(request, "larb/index.html")
    #
    #return render(request, '/larb/index.html')
