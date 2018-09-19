from django.shortcuts import render
from django.http import HttpResponseRedirect

def settings(request):
    return render(request, 'settings/settings.html')



#Show tables for new models
    
from django.views.generic import ListView


from settings.models import locations
from settings.models import clients
from settings.models import partners
from settings.models import skills

from settings.forms import locationForm
from settings.forms import partnerForm
from settings.forms import clientForm
from settings.forms import skillForm


#OUtdated...    
class locationList(ListView):
    model = locations
    
    
class clientList(ListView):
    model = clients
    
class partnerList(ListView):
    model = partners
    
class skillList(ListView):
    model = skills
#OUtdated^^^^
    
    
    


class LocationListView(ListView):
    template_name ='settings/locations_list.html'
    context_object_name = 'locations'
    model = locations


    
    def get(self, request, *args, **kwargs):
        # From FormMixin

        self.form = locationForm()

        # From ListView
        self.object_list = self.get_queryset()



        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request):
        
        form = locationForm(request.POST)
        if form.is_valid():
        # you should be able to extract inputs from the form here
            obj=locations()
            obj.name = form.cleaned_data['name']
            obj.save()
            return HttpResponseRedirect('/settings/locations/')
        else:
            form = locationForm()


class PartnerListView(ListView):
    template_name ='settings/partners_list.html'
    context_object_name = 'partners'
    model = partners


    
    def get(self, request, *args, **kwargs):
        # From FormMixin

        self.form = partnerForm()

        # From ListView
        self.object_list = self.get_queryset()



        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request):
        
        form = partnerForm(request.POST)
        if form.is_valid():
        # you should be able to extract inputs from the form here
            obj=partners()
            obj.name = form.cleaned_data['name']
            obj.save()
            return HttpResponseRedirect('/settings/partners/')
        else:
            form = partnerForm()
    


class ClientListView(ListView):
    template_name ='settings/clients_list.html'
    context_object_name = 'clients'
    model = clients


    
    def get(self, request, *args, **kwargs):
        # From FormMixin

        self.form = clientForm()

        # From ListView
        self.object_list = self.get_queryset()



        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request):
        
        form = clientForm(request.POST)
        if form.is_valid():
        # you should be able to extract inputs from the form here
            obj=clients()
            obj.name = form.cleaned_data['name']
            obj.save()
            return HttpResponseRedirect('/settings/clients/')
        else:
            form = clientForm()
    


class SkillListView(ListView):
    template_name ='settings/skills_list.html'
    context_object_name = 'skills'
    model = skills


    
    def get(self, request, *args, **kwargs):
        # From FormMixin

        self.form = skillForm()

        # From ListView
        self.object_list = self.get_queryset()



        context = self.get_context_data(object_list=self.object_list, form=self.form)
        return self.render_to_response(context)

    def post(self, request):
        
        form = skillForm(request.POST)
        if form.is_valid():
        # you should be able to extract inputs from the form here
            obj=skills()
            obj.name = form.cleaned_data['name']
            obj.save()
            return HttpResponseRedirect('/settings/skills/')
        else:
            form = skillForm()
        
    
