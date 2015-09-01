import requests
from django.shortcuts import render
from django.views.generic.base import View
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from .parser import *
from .forms import *


def stats_view(request):

    results = { }

    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            try:
                repo = form.cleaned_data["url"].split("/")
                if len(repo) == 5:
                    url = "https://api.github.com/repos/"+ repo[-2] +"/"+ repo[-1] + "/issues"
                    results = fetch_data(url) 
                else :
                    results = {"error":"Enter a valid repo URL (Ex:https://github.com/Shippable/support/)"}
            except:
                pass
        
    return render_to_response("dashboard.html", {"response":results}, context_instance=RequestContext(request))
