from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Expert, InputForm
from .search import search
import os

def home(request):
	
	experts = Expert.objects.all()
	return render(request, 'home.html', {'experts': experts})

def expert_detail(request,id):
	
	try:
		expert = Expert.objects.get(id=id)
	except Expert.DoesNotExist:
		raise Http404('Expert not found')
	return render(request, 'expert_detail.html', {'expert': expert})
			

def expert_search(request, min_num_skills=1):

	os.chdir(os.path.dirname(__file__)) 
	
	"""The following line is important. Results will be shown
	only if a test for expert=None is false. See templates/expert_search.html"""

	expert = None  #not needed
	experts = None
	if request.method == 'POST':
		"""user has provides input from web page"""
		form = InputForm(request.POST)
		if form.is_valid():
			form2 = form.save(commit=False)
			experts = search(form2.TQ, form2.min_num_skills)
	else:
		form = InputForm()

	return render(request,
                'expert_search.html',      #template to render
		{'form': form, 'expert': expert, 'experts':experts,},)
