from django.contrib import admin
from settings.models import skill_levels, partner_levels, client_levels, locations, skills, clients, partners, weeks, availability_levels
# Register your models here.


admin.site.register(skill_levels)
admin.site.register(partner_levels)
admin.site.register(client_levels)
admin.site.register(locations)
admin.site.register(skills)
admin.site.register(clients)
admin.site.register(partners)
admin.site.register(weeks)
admin.site.register(availability_levels)
