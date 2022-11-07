from django.shortcuts import render

# Create your views here.
def project_view(request):
    return render(request, "project_view.html")