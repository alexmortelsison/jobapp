from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
job_title = [
    "First job",
    "Second job"
]

job_description = [
    "First job description",
    "Second job description"
]

def hello(request):
    return HttpResponse("<h3>Hello World</h3>")

def job_detail(request, id):
    #return HttpResponse(f"<h1>Job detail page{id}</h1>")
    site = "https://google.com"
    return HttpResponse(f"Visit <a href={site}>Google here</a>")