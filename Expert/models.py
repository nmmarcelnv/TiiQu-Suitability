from django.db import models
from django.forms import ModelForm

class Expert(models.Model):
	
	"""This class defines an expert""" 
	GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
	name = models.CharField(
		max_length=30,
		blank=True)
	
	user_name = models.CharField(
		max_length=30,
		null=False, blank=False)
	
	gender = models.CharField(
		choices=GENDER_CHOICES, 
		max_length=1,
		blank=True)

	degree = models.CharField(
		max_length=30,
		null=False, blank=True)

	degree_subject = models.CharField(
		max_length=30,
		null=False, blank=True)

	current_role = models.CharField(
		max_length=30,
		blank=True)

	years_experience = models.IntegerField(
		blank=True, null=True)

	tq_value = models.FloatField(
		null=True)

	tq_score = models.FloatField(default=0,
		null=True)

	description = models.TextField(
		blank=True)

	membership_date	= models.DateTimeField(
		null=True, blank=True)

	skills = models.ManyToManyField('Skills', 
		blank=True)

	num_skills = models.IntegerField(default=0)


class Skills(models.Model):
	skill_name = models.CharField(max_length=50)

	def __str__(self):
		return self.skill_name



class Input(models.Model):

	TQ = models.FloatField(
		verbose_name=' Trust Quotient ', 
		default=0.0)

	skill1 = models.CharField(verbose_name=' Skill #1 ',
		max_length=50, blank=True)
 
	skill2 = models.CharField(verbose_name=' Skill #2 ',
		max_length=50, blank=True) 

	skill3 = models.CharField(verbose_name=' Skill #3 ',
		max_length=50, blank=True)

	skill4 = models.CharField(verbose_name=' Skill #4 ',
		max_length=50, blank=True)

	skill5 = models.CharField(verbose_name=' Skill #5 ',
		max_length=50, blank=True)

	degree = models.CharField(max_length=50, 
		blank=True) 

	min_num_skills = models.IntegerField(verbose_name=' Minimum Number of Skills ',
		default=1)
	years_experience = models.IntegerField(default=0)	


class InputForm(ModelForm):
        class Meta:
                model = Input
                fields = "__all__"

