from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from Expert.models import Expert, Skills
from pytz import UTC


DATETIME_FORMAT = '%m/%d/%Y %H:%M'

SKILLS_NAMES = [
    'Programming',
    'Java', 
    'Web Development',
    'Linux',
    'Teaching',
    'Leadership',
    'Communication',
    'Public Speaking',
    'Data Analysis',
    'Project Management',
    'Problem Solving',
    'Research',
    'Machine Learning'
]

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the expert data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
	# Show this when the user types help
	help = "Loads data from expert_data.csv into our Expert model"

	def handle(self, *args, **options):
		if Expert.objects.exists() or Skills.objects.exists():
			print('Expert data already loaded...exiting.')
			print(ALREADY_LOADED_ERROR_MESSAGE)
			return
		print("Generating  List of Skills")
		for skill_name in SKILLS_NAMES:
			skill = Skills(skill_name=skill_name)
			skill.save()
		print("Loading data for experts available for hire")
		for row in DictReader(open('./expert_data.csv')):
			expert = Expert()
			expert.name = row['Expert']
			expert.user_name = row['User Name']
			expert.degree = row['Degree']
			expert.degree_subject = row['Subject']
			expert.current_role = row['Occupation']
			expert.gender = row['Gender']
			expert.years_experience = row['Years of Experience']
			expert.tq_value = row['TQ value'] 
			expert.description = row['Short Description']
			expert.num_skills = row['Number of Skills']
			raw_membership_date = row['Membership Date'] 
			membership_date = UTC.localize(
				datetime.strptime(raw_membership_date, DATETIME_FORMAT))
			expert.membership_date = membership_date
			expert.save()
			#print(expert.membership_date)
			raw_skill_names = row['Skills']
			skill_names = [name for name in raw_skill_names.split('| ') if name]
			for skill_name in skill_names:
				skill = Skills.objects.get(skill_name=skill_name)
				expert.skills.add(skill)
			expert.save()
