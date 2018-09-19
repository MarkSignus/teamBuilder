from django.shortcuts import render
from django.http import HttpResponseRedirect

    
from django.views.generic import ListView


from associates.models import associate_table
from associates.models import assoc_partner_relationship,assoc_client_relationship,assoc_skills

from associates.forms import associateForm, assoc_partnerForm,assoc_clientForm,assoc_skillForm


class assoc_skill_List(ListView):
    template_name ='associates/assoc_skill.html'
    context_object_name = 'assoc_skill'
    model = assoc_skills


    
    def get(self, request, *args, **kwargs):
        # From FormMixin

        self.form = assoc_skillForm()

        # From ListView
        self.object_list = self.get_queryset()



        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request):
        
        form = assoc_skillForm(request.POST)
        if form.is_valid():
        # you should be able to extract inputs from the form here
            obj=assoc_skills()
            obj.name = form.cleaned_data['associate_id']
            obj.name = form.cleaned_data['skill_id']
            obj.name = form.cleaned_data['level']
            obj.save()
            return HttpResponseRedirect('/associates/assoc_skill/')
        else:
            form = assoc_skillForm()






class assoc_client_relationship_List(ListView):
    template_name ='associates/assoc_client.html'
    context_object_name = 'assoc_client'
    model = assoc_client_relationship


    
    def get(self, request, *args, **kwargs):
        # From FormMixin

        self.form = assoc_clientForm()

        # From ListView
        self.object_list = self.get_queryset()



        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request):
        
        form = assoc_clientForm(request.POST)
        if form.is_valid():
        # you should be able to extract inputs from the form here
            obj=assoc_client_relationship()
            obj.name = form.cleaned_data['associate_id']
            obj.name = form.cleaned_data['client_id']
            obj.name = form.cleaned_data['level']
            obj.save()
            return HttpResponseRedirect('/associates/assoc_client/')
        else:
            form = assoc_clientForm()



class assoc_partner_relationship_List(ListView):
    template_name ='associates/assoc_partner.html'
    context_object_name = 'assoc_partner'
    model = assoc_partner_relationship


    
    def get(self, request, *args, **kwargs):
        # From FormMixin

        self.form = assoc_partnerForm()

        # From ListView
        self.object_list = self.get_queryset()



        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request):
        
        form = assoc_partnerForm(request.POST)
        if form.is_valid():
        # you should be able to extract inputs from the form here
            obj=assoc_partner_relationship()
            obj.name = form.cleaned_data['associate_id']
            obj.name = form.cleaned_data['partner_id']
            obj.name = form.cleaned_data['level']
            obj.save()
            return HttpResponseRedirect('/associates/assoc_partner/')
        else:
            form = assoc_partnerForm()
    
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