from django.contrib import admin


from associates.models import associate_table, assoc_client_relationship, assoc_skills, assoc_partner_relationship,assoc_availability



admin.site.register(associate_table)
admin.site.register(assoc_client_relationship)
admin.site.register(assoc_skills)
admin.site.register(assoc_partner_relationship)
admin.site.register(assoc_availability)
