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
    """ Django view to take github repo url as input and fetch issues data for the repo using Github API's """

    #default value to handle invalid input or no input value
    results = {"error":"Enter a valid repo URL (Example:https://github.com/Shippable/support/)"}
    form = IssueForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        url = form.cleaned_data["url"].rstrip('/') #remove trailing slash if any
        repo = url.split("/") #split url to get user and repo name
        
        #check for valid repo url
        if len(repo) == 5:
            url = "https://api.github.com/repos/"+ repo[-2] +"/"+ repo[-1] + "/issues"
            results = fetch_data(url) 

    return render_to_response("dashboard.html", {"response":results}, context_instance=RequestContext(request))
