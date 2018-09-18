from django.contrib import admin
from settings.models import skill_levels
from settings.models import partner_levels
from settings.models import client_levels
from settings.models import locations
from settings.models import skills
from settings.models import clients
from settings.models import partners
# Register your models here.


admin.site.register(skill_levels)
admin.site.register(partner_levels)
admin.site.register(client_levels)
admin.site.register(locations)
admin.site.register(skills)
admin.site.register(clients)
admin.site.register(partners)
