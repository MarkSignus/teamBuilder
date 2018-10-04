from django.http import HttpResponseRedirect  
from django.views.generic import ListView



from projects.models import proj_table, proj_partner_relationship, proj_client_relationship, proj_skills, proj_associates

from projects.forms import projForm, proj_partnerForm, proj_clientForm, proj_skillForm, proj_assocForm

from associates.models import associate_table
from associates.models import assoc_partner_relationship,assoc_client_relationship,assoc_skills,assoc_availability


from django.core.exceptions import ObjectDoesNotExist
            
import cvxpy as cvx
import pandas as pd
from projects.Optimizer import norm_var, def_avail, def_clientR, def_partnerR, def_skills, calc_weights, compile_objectives, add_variable_absHC


def get_or_none(queryset, *args, **kwargs):
    try:
        return queryset.get(*args, **kwargs)
    except ObjectDoesNotExist:
        return None

class proj_assoc_List(ListView):
    template_name ='projects/proj_associates.html'
    context_object_name = 'proj_associates'
    model = proj_associates
    
    
    def get(self, request,q, *args, **kwargs):
        # From FormMixin

        self.form = proj_assocForm()
        
        proj_model = proj_table.objects.get(id=q)
        skills_model = proj_skills.objects.filter(project_id=q)
        client_model = proj_client_relationship.objects.filter(project_id=q)
        partner_model = proj_partner_relationship.objects.filter(project_id=q)
        assoc_model = associate_table.objects.all()
        #assoc_skills_model = assoc_skills.objects.all()     
        #assoc_client_model = assoc_client_relationship.objects.all()     
        #assoc_partner_model = assoc_partner_relationship.objects.all()
        #assoc_avail_model = assoc_availability.objects.all()
       

        
        
        #Dictionaries to hold associate info
        avail_dicts=dict()
        client_dicts=dict()
        partner_dicts=dict()
        skill_dicts=dict()
        assoc_indexes=[]
        
        #Store isMin values
        client_isMin=dict()
        partner_isMin=dict()
        skill_isMin=dict()
        
        #Store limits
        client_limits=dict()
        partner_limits=dict()
        skill_limits=dict()
        
        #Get all associate info
        num_assocs=0
        for j in assoc_model:
            num_assocs+=1
            assoc_indexes.append(j.id)
            
            #Get availability info 
            for i in range(1,(proj_model.duration+1)):
                avail_val=assoc_availability.objects.filter(associate_id=j.id,week_id=i).first()
                    
                if avail_val==None:
                    current_avail=1 #Default assume 1, can change this
                else: 
                    current_avail =avail_val.level.value
                    
                current_avail_key='avail_wk'+str(i)
                if current_avail_key in avail_dicts:
                    avail_dicts[current_avail_key].append(int(current_avail))
                else:
                    avail_dicts[current_avail_key]=[int(current_avail)]
                
        
                
            #Get client info 
            for i in client_model:
                client_val = assoc_client_relationship.objects.filter(associate_id=j.id,client_id=i.id).first()

                    
                if client_val==None:
                    current_client=1 #Default assume 1, can change this
                else: 
                    current_client =client_val.level.value
                    
                current_client_key='client_'+str(i.id)
                if current_client_key in client_dicts:
                    client_dicts[current_client_key].append(current_client)
                else:
                    client_dicts[current_client_key]=[current_client]
                
                #get isMin value 
                client_isMin[current_client_key]=i.isMin
                
                #get limit
                client_limits[current_client_key]={'min' : i.minimum.value}
                
                
            #Get partner info 

            for i in partner_model:
                partner_val=assoc_partner_relationship.objects.filter(associate_id=j.id,partner_id=i.id).first()
                    
                if partner_val==None:
                    current_partner=1 #Default assume 1, can change this
                else: 
                    current_partner =partner_val.level.value
                    
                current_partner_key='partner_'+str(i.id)
                if current_partner_key in partner_dicts:
                    partner_dicts[current_partner_key].append(current_partner)
                else:
                    partner_dicts[current_partner_key]=[current_partner]

                #get isMin value 
                partner_isMin[current_partner_key]=i.isMin 
                
                #get limit
                partner_limits[current_partner_key]={'min' : i.minimum.value}
            
            #Get skill info 

            for i in skills_model:
                skill_val=assoc_skills.objects.filter(associate_id=j.id,skill_id=i.id).first()
                    
                if skill_val==None:
                    current_skill=1 #Default assume 1, can change this
                else: 
                    current_skill =skill_val.level.value
                    
                current_skill_key='skill_'+str(i.id)
                if current_skill_key in skill_dicts:
                    skill_dicts[current_skill_key].append(current_skill)
                else:
                    skill_dicts[current_skill_key]=[current_skill]

                #get isMin value 
                skill_isMin[current_skill_key]=i.isMin
                
                #get limit
                skill_limits[current_skill_key]={'min' : i.minimum.value}        
        
        
        
        
        #get weight - NEED TO UPDATE WHEN USER INPUTS ADDED
        weigths_info_dict={**client_dicts,**partner_dicts,**skill_dicts}
        
        weights={'availability' : 5}
        for k,v in weigths_info_dict.items():
             
            sign=1
            
            if k in client_isMin:
                if client_isMin[k]==True:
                    sign=-1
            elif k in partner_isMin:
                if partner_isMin[k]==True:
                    sign=-1                
            elif k in skill_isMin:
                if skill_isMin[k]==True:
                    sign=-1                
            weights[k]=(5*sign) #Set all to 5 for now, will become importance input

        #Limits dictionary
        limits = {**client_limits,**partner_limits,**skill_limits}




        #Save all associate info
        associates_info_dict={**avail_dicts,**weigths_info_dict}
        data = pd.DataFrame(associates_info_dict,
                            index = assoc_indexes)
        
        
 #=============================================================================
        x = cvx.Variable(num_assocs, boolean=True)
        
        #Calc weights normalizes the weights and splits it into 4 variables for avail,client,partner,skill
        wA, wC, wP, wS = calc_weights(weights)
        
        #Create the variables that go into the objective function
        vA, cA = def_avail(x, data, proj_model.duration, wA) 
        vS, cS = def_skills(x, data, wS)
        vC, cC = def_clientR(x, data, wC) 
        vP, cP = def_partnerR(x, data, wP)


        
        #Create hard constraints
        aux, HClist = add_variable_absHC(x, data, limits)
        
        #Compile objective
        objs = {}
        objs.update(vC)
        objs.update(vP)
        objs.update(vS)
        objs.update(vA)
        
       #Create Objective Func
        obj = compile_objectives(objs)
        
        #Compile constraints
        constraints = []
        constraints.extend(cC)
        constraints.extend(cP)
        constraints.extend(cS)
        constraints.extend(cA)
        constraints.extend(HClist) 
        constraints.extend([sum(x) == proj_model.team_size]) 
        
        #Generate optimization problem
        p = cvx.Problem(obj, constraints)
        p.solve()
        
#         #See solution
        choices=pd.Series([round(x[num].value) for num in range(0,(num_assocs),1)], index = data.index)     
        chosen_assocs=list(choices.iloc[choices.nonzero()].index)
# =============================================================================



        # Get chosen associates
        self.object_list = associate_table.objects.filter(id__in=chosen_assocs)
    
        context = self.get_context_data(object_list=self.object_list, form=self.form, modelone=proj_model)
        return self.render_to_response(context)
    
    
    #IGnore for now
    def post(self, request,q):
        
        form = proj_assocForm(request.POST)
        if form.is_valid():
        # you should be able to extract inputs from the form here
            obj=proj_associates()
            obj.project_id = form.cleaned_data['project_id']
            obj.associate_id = form.cleaned_data['associate_id']
            obj.save()
            return HttpResponseRedirect('/projects/proj_associates/'+str(q))
        else:
            return HttpResponseRedirect('/projects/proj_associates/'+str(q))






    

 #=============================================================================




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
            return HttpResponseRedirect('/projects/proj_skill/'+str(q))
        else:
            return HttpResponseRedirect('/projects/proj_skill/'+str(q))





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
            obj=proj_table()
            obj.name = form.cleaned_data['name']
            obj.location = form.cleaned_data['location']
            obj.duration = form.cleaned_data['duration']
            obj.fee = form.cleaned_data['fee']
            obj.team_size = form.cleaned_data['team_size']
            obj.save()
            return HttpResponseRedirect('/projects/')
        else:
            form = projForm()