from django.shortcuts import render
from django.http import HttpResponseRedirect

    
from django.views.generic import ListView


from associates.models import associate_table
from associates.models import assoc_partner_relationship,assoc_client_relationship,assoc_skills,assoc_availability

from associates.forms import associateForm, assoc_partnerForm,assoc_clientForm,assoc_skillForm,assoc_availForm


class assoc_skill_List(ListView):
    template_name ='associates/assoc_skill.html'
    context_object_name = 'assoc_skill'
    model = assoc_skills
    

    def get_queryset(self,fil, *args, **kwargs):
        qs = assoc_skills.objects.all()
        qs = qs.filter(associate_id=fil)
        return qs
    
    def get(self, request,q, *args, **kwargs):
        # From FormMixin

        self.form = assoc_skillForm()

        # From ListView
        self.object_list = self.get_queryset(fil=q)


        context = self.get_context_data(object_list=self.object_list, form=self.form, modelone = associate_table.objects.get(id=q))
        return self.render_to_response(context)
    

    def post(self, request,q):
        
        form = assoc_skillForm(request.POST)
        if form.is_valid():
        # you should be able to extract inputs from the form here
            obj=assoc_skills()
            obj.associate_id = form.cleaned_data['associate_id']
            obj.skill_id = form.cleaned_data['skill_id']
            obj.level = form.cleaned_data['level']
            obj.save()
            return HttpResponseRedirect('/associates/assoc_skill/'+str(q))
        else:
            return HttpResponseRedirect('/associates/assoc_skill/'+str(q))



class assoc_avail_List(ListView):
    template_name ='associates/assoc_availability.html'
    context_object_name = 'assoc_availability'
    model = assoc_availability
    

    def get_queryset(self,fil, *args, **kwargs):
        qs = assoc_availability.objects.all()
        qs = qs.filter(associate_id=fil)
        return qs
    
    def get(self, request,q, *args, **kwargs):
        # From FormMixin

        self.form = assoc_availForm()

        # From ListView
        self.object_list = self.get_queryset(fil=q)


        context = self.get_context_data(object_list=self.object_list, form=self.form, modelone = associate_table.objects.get(id=q))
        return self.render_to_response(context)
    

    def post(self, request,q):
        
        form = assoc_availForm(request.POST)
        if form.is_valid():
        # you should be able to extract inputs from the form here
            obj=assoc_availability()
            obj.associate_id = form.cleaned_data['associate_id']
            obj.week_id = form.cleaned_data['week_id']
            obj.level = form.cleaned_data['level']
            obj.save()
            return HttpResponseRedirect('/associates/assoc_availability/'+str(q))
        else:
            return HttpResponseRedirect('/associates/assoc_availability/'+str(q))






class assoc_client_relationship_List(ListView):
    template_name ='associates/assoc_client.html'
    context_object_name = 'assoc_client'
    model = assoc_client_relationship
    


    def get_queryset(self,fil, *args, **kwargs):
        qs = assoc_client_relationship.objects.all()
        qs = qs.filter(associate_id=fil)
        return qs
    
    
    def get(self, request,q, *args, **kwargs):
        # From FormMixin

        self.form = assoc_clientForm()

        # From ListView
        self.object_list = self.get_queryset(fil=q)



        context = self.get_context_data(object_list=self.object_list, form=self.form, modelone = associate_table.objects.get(id=q))
        return self.render_to_response(context)
    
    

    def post(self, request,q):
        
        form = assoc_clientForm(request.POST)
        if form.is_valid():
        # you should be able to extract inputs from the form here
            obj=assoc_client_relationship()
            obj.associate_id = form.cleaned_data['associate_id']
            obj.client_id = form.cleaned_data['client_id']
            obj.level = form.cleaned_data['level']
            obj.save()
            return HttpResponseRedirect('/associates/assoc_client/'+str(q))
        else:
            return HttpResponseRedirect('/associates/assoc_client/'+str(q))



class assoc_partner_relationship_List(ListView):
    template_name ='associates/assoc_partner.html'
    context_object_name = 'assoc_partner'
    model = assoc_partner_relationship

    def get_queryset(self,fil, *args, **kwargs):
        qs = assoc_partner_relationship.objects.all()
        qs = qs.filter(associate_id=fil)
        return qs
    
    def get(self, request,q, *args, **kwargs):
        # From FormMixin

        self.form = assoc_partnerForm()

        # From ListView
        self.object_list = self.get_queryset(fil=q)



        context = self.get_context_data(object_list=self.object_list, form=self.form, modelone = associate_table.objects.get(id=q))
        return self.render_to_response(context)

    def post(self, request,q):
        
        form = assoc_partnerForm(request.POST)
        if form.is_valid():
        # you should be able to extract inputs from the form here
            obj=assoc_partner_relationship()
            obj.associate_id = form.cleaned_data['associate_id']
            obj.partner_id = form.cleaned_data['partner_id']
            obj.level = form.cleaned_data['level']
            obj.save()
            return HttpResponseRedirect('/associates/assoc_partner/'+str(q))
        else:
            return HttpResponseRedirect('/associates/assoc_partner/'+str(q))
    
class AssociateListView(ListView):
    template_name ='associates/associate_list.html'
    context_object_name = 'associates'
    model = associate_table


    
    def get(self, request, *args, **kwargs):
        # From FormMixin

        self.form = associateForm()

        # From ListView
        self.object_list = self.get_queryset()



        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request):
        
        form = associateForm(request.POST)
        if form.is_valid():
        # you should be able to extract inputs from the form here
            obj=associate_table()
            obj.name = form.cleaned_data['name']
            obj.location = form.cleaned_data['location']
            obj.rate = form.cleaned_data['rate']
            obj.save()
            return HttpResponseRedirect('/associates/')
        else:
            form = associateForm()