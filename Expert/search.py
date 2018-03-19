from .models import Expert
from django.http import Http404
import os

def search(TQ, min_num_skills=1):

	"""inputs:
		float TQ: The user's Trust Quotien
		min_num_skills: minimum number of skills desired
	"""

	try:
		experts = Expert.objects.all()
	except Expert.DoesNotExist:
		raise Http404('Expert not found') 

	avg_num_skills = get_avg_num_skills(experts) 
	experts = get_tq_score(experts, avg_num_skills)

	
	"""For order_by and filter examples, see:
	https://docs.djangoproject.com/en/2.0/ref/models/querysets/
	"""
	
	exps = (Expert.objects.filter(tq_value__gte = TQ).
		order_by('-tq_score').
		filter(num_skills__gte = min_num_skills))
	
	"""get the top 5, most popular experts"""
	experts_search_result = exps.all()[0:5]

	return list(experts_search_result)


def get_avg_num_skills(experts):
	
	sum_skills = 0
	for expert in experts:
		sum_skills += expert.num_skills
	return sum_skills/len(experts)


def get_tq_score(experts,avg_num_skills):

	"""
	This function calculates the weighted Trust Quoting (TQ)
		
	"""
	
	for expert in experts:
		expert.tq_score = expert.tq_value*(expert.num_skills/avg_num_skills)

		"""save the state, otherwise changes will not be effected. see:
		https://docs.djangoproject.com/en/2.0/ref/models/querysets/#id4
		"""
		expert.save()
	return experts



def get_weighted_tq(experts, avg_num_skills, min_num_skills=1):

	#This function is not being used currently	
	for expert in experts:
		TQ = expert.tq_value
		num_skills = expert.num_skills
		expert.tq_score = ((num_skills*TQ)/(num_skills+min_num_skills)) + ((min_num_skills*avg_num_skills)/(num_skills+min_num_skills)) 
		
		"""save the state, otherwise changes will not be effected. see:
		https://docs.djangoproject.com/en/2.0/ref/models/querysets/#id4
		"""
		expert.save()
	return experts

