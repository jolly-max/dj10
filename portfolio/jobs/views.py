from django.shortcuts import render

# Create your views here.
def home(request):
    jobs=Job.object.all
    return render(request, "jobs/home.html", {"jobs":jobs})
    add.blog