from django.shortcuts import render

# Create your views here.
def contract_view(request):
	return render(request, "contract_view.html")

def documentations_view(request):
	return render(request, "documentations_view.html")

def doc1(request):
	return render(request, "doc1.html")

def doc2(request):
	return render(request, "doc2.html")

def doc3(request):
	return render(request, "doc3.html")

def doc4(request):
	return render(request, "doc4.html")

def doc5(request):
	return render(request, "doc5.html")

def plan(request):
	return render(request, "plan.html")