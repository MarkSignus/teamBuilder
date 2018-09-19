from django import forms
from settings.models import locations
from settings.models import partners
from settings.models import clients
from settings.models import skills


class locationForm(forms.ModelForm):

    name = forms.CharField(label='Location name',max_length=50,widget=forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = locations
        fields = ('name',)
        
class partnerForm(forms.ModelForm):

    name = forms.CharField(label='Parter name',max_length=50,widget=forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = partners
        fields = ('name',)
        
        
class clientForm(forms.ModelForm):

    name = forms.CharField(label='Client name',max_length=50,widget=forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = clients
        fields = ('name',)
        
        
class skillForm(forms.ModelForm):

    name = forms.CharField(label='Skill name',max_length=50,widget=forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = skills
        fields = ('name',)