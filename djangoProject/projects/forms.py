from django import forms
from projects.models import proj_table, proj_client_relationship,proj_skills,proj_associates,proj_partner_relationship
from settings.models import locations,clients,client_levels, skills, skill_levels, partners, partner_levels
from associates.models import associate_table

TRUE_FALSE_CHOICES = (
    (True, 'Foster Development'),
    (False, 'Prefer Experience')
)



class projForm(forms.ModelForm):
    name=forms.CharField(
        label='Name',
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter project name..'
            }
        ))
    duration=forms.IntegerField(
        label='Duration',
        widget=forms.NumberInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter project duration (# of weeks)..'
            }
        ))
    location = forms.ModelChoiceField(label='Location',queryset=locations.objects,widget=forms.Select(attrs={'class' : 'form-control'}))
    fee=forms.IntegerField(
        label='Fee',
        widget=forms.NumberInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Enter the fee in GBP (thousands)'
            }
        ))

    class Meta:
        model = proj_table
        fields = '__all__'

class proj_assocForm(forms.ModelForm):

    associate_id = forms.ModelChoiceField(label='Associate',queryset=associate_table.objects,widget=forms.Select(attrs={'class' : 'form-control'}))
    project_id = forms.ModelChoiceField(label='Project',queryset=proj_table.objects,widget=forms.Select(attrs={'class' : 'form-control'}))

    class Meta:
        model = proj_associates
        fields = '__all__'


class proj_partnerForm(forms.ModelForm):

    project_id = forms.ModelChoiceField(label='Project',queryset=proj_table.objects,widget=forms.Select(attrs={'class' : 'form-control'}))
    partner_id = forms.ModelChoiceField(label='Partner',queryset=partners.objects,widget=forms.Select(attrs={'class' : 'form-control'}))
    minimum = forms.ModelChoiceField(label='Min Level',queryset=partner_levels.objects,widget=forms.Select(attrs={'class' : 'form-control'}))
    isMin = forms.ChoiceField(label='Minimise',choices = TRUE_FALSE_CHOICES, widget=forms.Select(attrs={'class' : 'form-control'}))

    class Meta:
        model = proj_partner_relationship
        fields = '__all__'


class proj_clientForm(forms.ModelForm):

    project_id = forms.ModelChoiceField(label='Project',queryset=proj_table.objects,widget=forms.Select(attrs={'class' : 'form-control'}))
    client_id = forms.ModelChoiceField(label='Client',queryset=clients.objects,widget=forms.Select(attrs={'class' : 'form-control'}))
    minimum = forms.ModelChoiceField(label='Min Level',queryset=client_levels.objects,widget=forms.Select(attrs={'class' : 'form-control'}))
    isMin = forms.ChoiceField(label='Minimise',choices = TRUE_FALSE_CHOICES, widget=forms.Select(attrs={'class' : 'form-control'}))

    class Meta:
        model = proj_client_relationship
        fields = '__all__'


class proj_skillForm(forms.ModelForm):

    project_id = forms.ModelChoiceField(label='Project',queryset=proj_table.objects,widget=forms.Select(attrs={'class' : 'form-control'}))
    skill_id = forms.ModelChoiceField(label='Skill',queryset=skills.objects,widget=forms.Select(attrs={'class' : 'form-control'}))
    minimum = forms.ModelChoiceField(label='Min Level',queryset=skill_levels.objects,widget=forms.Select(attrs={'class' : 'form-control'}))
    isMin = forms.ChoiceField(label='Minimise',choices = TRUE_FALSE_CHOICES, widget=forms.Select(attrs={'class' : 'form-control'}))

    class Meta:
        model = proj_skills
        fields = '__all__'
