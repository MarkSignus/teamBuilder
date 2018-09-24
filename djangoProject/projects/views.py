from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.db import connection
    
from django.views.generic import ListView


from associates.models import associate_table
from projects.models import proj_table, proj_partner_relationship, proj_client_relationship, proj_skills, proj_associates

from projects.forms import projForm, proj_partnerForm, proj_clientForm, proj_skillForm, proj_assocForm


class proj_skill_List(ListView):
    template_name ='projects/proj_skill.html'
    context_object_name = 'proj_skill'
    model = proj_skills
    

    def get_queryset(self,fil, *args, **kwargs):
        qs = proj_skills.objects.all()
        qs = qs.filter(project_id=fil)
        return qs
    
    def get(self, request,q, *args, **kwargs):
        # From FormMixin

        self.form = proj_skillForm()

        # From ListView
        self.object_list = self.get_queryset(fil=q)


        context = self.get_context_data(object_list=self.object_list, form=self.form, modelone = proj_table.objects.get(id=q))
        return self.render_to_response(context)
    

    def post(self, request,q):
        
        form = proj_skillForm(request.POST)
        if form.is_valid():
        # you should be able to extract inputs from the form here
            obj=proj_skills()
            obj.project_id = form.cleaned_data['project_id']
            obj.skill_id = form.cleaned_data['skill_id']
            obj.minimum = form.cleaned_data['minimum']
            obj.isMin = form.cleaned_data['isMin']
            obj.save()
            return HttpResponseRedirect('/project/proj_skill/'+str(q))
        else:
            return HttpResponseRedirect('/project/proj_skill/'+str(q))



class proj_assoc_List(ListView):
    template_name ='projects/proj_associates.html'
    context_object_name = 'proj_associates'
    model = proj_associates
    

    def get_queryset(self,fil, *args, **kwargs):
        qs = proj_associates.objects.all()
        qs = qs.filter(project_id=fil)
        return qs
    
    def get(self, request,q, *args, **kwargs):
        # From FormMixin

        self.form = proj_assocForm()

        # From ListView
        self.object_list = self.get_queryset(fil=q)


        context = self.get_context_data(object_list=self.object_list, form=self.form, modelone = proj_table.objects.get(id=q))
        return self.render_to_response(context)
    

    def post(self, request,q):
        
        form = proj_assocForm(request.POST)
        if form.is_valid():
        # you should be able to extract inputs from the form here
            obj=proj_associates()
            obj.project_id = form.cleaned_data['project_id']
            obj.associate_id = form.cleaned_data['associate_id']
            obj.save()
            return HttpResponseRedirect('/project/proj_associates/'+str(q))
        else:
            return HttpResponseRedirect('/project/proj_associates/'+str(q))






class proj_client_relationship_List(ListView):
    template_name ='projects/proj_client.html'
    context_object_name = 'proj_client'
    model = proj_client_relationship
    


    def get_queryset(self,fil, *args, **kwargs):
        qs = proj_client_relationship.objects.all()
        qs = qs.filter(project_id=fil)
        return qs
    
    
    def get(self, request,q, *args, **kwargs):
        # From FormMixin

        self.form = proj_clientForm()

        # From ListView
        self.object_list = self.get_queryset(fil=q)



        context = self.get_context_data(object_list=self.object_list, form=self.form, modelone = proj_table.objects.get(id=q))
        return self.render_to_response(context)
    
    

    def post(self, request,q):
        
        form = proj_clientForm(request.POST)
        if form.is_valid():
        # you should be able to extract inputs from the form here
            obj=proj_client_relationship()
            obj.project_id = form.cleaned_data['project_id']
            obj.client_id = form.cleaned_data['client_id']
            obj.minimum = form.cleaned_data['minimum']
            obj.isMin = form.cleaned_data['isMin']
            obj.save()
            return HttpResponseRedirect('/projects/proj_client/'+str(q))
        else:
            return HttpResponseRedirect('/projects/proj_client/'+str(q))



class proj_partner_relationship_List(ListView):
    template_name ='projects/proj_partner.html'
    context_object_name = 'proj_partner'
    model = proj_partner_relationship

    def get_queryset(self,fil, *args, **kwargs):
        qs = proj_partner_relationship.objects.all()
        qs = qs.filter(project_id=fil)
        return qs
    
    def get(self, request,q, *args, **kwargs):
        # From FormMixin

        self.form = proj_partnerForm()

        # From ListView
        self.object_list = self.get_queryset(fil=q)



        context = self.get_context_data(object_list=self.object_list, form=self.form, modelone = proj_table.objects.get(id=q))
        return self.render_to_response(context)

    def post(self, request,q):
        
        form = proj_partnerForm(request.POST)
        if form.is_valid():
        # you should be able to extract inputs from the form here
            obj=proj_partner_relationship()
            obj.project_id = form.cleaned_data['project_id']
            obj.partner_id = form.cleaned_data['partner_id']
            obj.minimum = form.cleaned_data['minimum']
            obj.isMin = form.cleaned_data['isMin']
            obj.save()
            return HttpResponseRedirect('/projects/proj_partner/'+str(q))
        else:
            return HttpResponseRedirect('/projects/proj_partner/'+str(q))
    
class ProjectListView(ListView):
    template_name ='projects/proj_list.html'
    context_object_name = 'projects'
    model = proj_table


    
    def get(self, request, *args, **kwargs):
        # From FormMixin

        self.form = projForm()

        # From ListView
        self.object_list = self.get_queryset()



        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request):
        
        form = projForm(request.POST)
        if form.is_valid():
        # you should be able to extract inputs from the form here
            obj=associate_table()
            obj.name = form.cleaned_data['name']
            obj.location = form.cleaned_data['location']
            obj.duration = form.cleaned_data['duration']
            obj.fee = form.cleaned_data['fee']
            obj.save()
            return HttpResponseRedirect('/projects/')
        else:
            form = projForm()