from django.contrib import admin


from associates.models import associate_table
from associates.models import assoc_client_relationship
from associates.models import assoc_skills
from associates.models import assoc_partner_relationship



admin.site.register(associate_table)
admin.site.register(assoc_client_relationship)
admin.site.register(assoc_skills)
admin.site.register(assoc_partner_relationship)
