from django.shortcuts import render

# Create your views here.
def contract_view(request):
	return render(request, "contract_view.html")
