from django import forms
from associates.models import associate_table, assoc_partner_relationship,assoc_client_relationship,assoc_skills
from settings.models import locations,clients,client_levels, skills, skill_levels, partners, partner_levels


class associateForm(forms.ModelForm):
    name=forms.CharField(label='Name',max_length=50,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    location = forms.ModelChoiceField(label='Location',queryset=locations.objects,widget=forms.Select(attrs={'class' : 'form-control'}))
    rate=forms.IntegerField(label='Rate',widget=forms.NumberInput(attrs={'class' : 'form-control'}))
    
    class Meta:
        model = associate_table
        fields = '__all__' 
        

class assoc_partnerForm(forms.ModelForm):

    associate_id = forms.ModelChoiceField(label='Associate',queryset=associate_table.objects,widget=forms.Select(attrs={'class' : 'form-control'}))
    partner_id = forms.ModelChoiceField(label='Partner',queryset=partners.objects,widget=forms.Select(attrs={'class' : 'form-control'}))
    level = forms.ModelChoiceField(label='Level',queryset=partner_levels.objects,widget=forms.Select(attrs={'class' : 'form-control'}))

    class Meta:
        model = assoc_partner_relationship
        fields = '__all__'


class assoc_clientForm(forms.ModelForm):

    associate_id = forms.ModelChoiceField(label='Associate',queryset=associate_table.objects,widget=forms.Select(attrs={'class' : 'form-control'}))
    client_id = forms.ModelChoiceField(label='Client',queryset=clients.objects,widget=forms.Select(attrs={'class' : 'form-control'}))
    level = forms.ModelChoiceField(label='Level',queryset=client_levels.objects,widget=forms.Select(attrs={'class' : 'form-control'}))

    class Meta:
        model = assoc_client_relationship
        fields = '__all__'


class assoc_skillForm(forms.ModelForm):

    associate_id = forms.ModelChoiceField(label='Associate',queryset=associate_table.objects,widget=forms.Select(attrs={'class' : 'form-control'}))
    skill_id = forms.ModelChoiceField(label='Skill',queryset=skills.objects,widget=forms.Select(attrs={'class' : 'form-control'}))
    level = forms.ModelChoiceField(label='Level',queryset=skill_levels.objects,widget=forms.Select(attrs={'class' : 'form-control'}))

    class Meta:
        model = assoc_skills
        fields = '__all__'


        