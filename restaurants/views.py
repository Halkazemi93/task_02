from django.shortcuts import render

def greetings(request):
	context = {
		"msg": "Hello World!",


	}
	return render(request, 'task02.html', context)
# Create your views here.
