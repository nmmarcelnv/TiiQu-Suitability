from django.contrib import admin

"""Use the Django admin to create administrative 
privileges for Expert data. an Admin will be able
to see and modify expert data"""

# we need to import the Expert class
from .models import Expert

"""create a class for the admin interface.
the class needs to be registered with admin
to tell it which model it's associated with"""
@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
	list_display = ['name',
			'user_name',
			'gender',
			'membership_date',
			'degree',
			'degree_subject', 
			'tq_value']
