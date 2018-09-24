from django.contrib import admin


from projects.models import proj_table, proj_client_relationship, proj_skills, proj_partner_relationship,proj_associates



admin.site.register(proj_table)
admin.site.register(proj_client_relationship)
admin.site.register(proj_skills)
admin.site.register(proj_partner_relationship)
admin.site.register(proj_associates)
