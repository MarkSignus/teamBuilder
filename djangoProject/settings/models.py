from django.db import models, migrations

# Create your models here.


#LOCATIONS
class locations(models.Model):
    class Meta:
        verbose_name_plural = "locations"
    name = models.CharField(max_length =50, default ='',blank=False,null=False)
    
 
    
#CLIENTS
class clients(models.Model):
    class Meta:
        verbose_name_plural = "clients"
    name = models.CharField(max_length =50, default ='',blank=False,null=False)

    
#PARTNERS  
class partners(models.Model):
    class Meta:
        verbose_name_plural = "partners"
    name = models.CharField(max_length =50, default ='',blank=False,null=False)
    
    
#SKILLS  
class skills(models.Model):
    class Meta:
        verbose_name_plural = "skills"
    name = models.CharField(max_length =50, default ='',blank=False,null=False)
    

#SKILL LEVELS
class skill_levels(models.Model):
    class Meta:
        verbose_name_plural = "skill_levels"
    value = models.IntegerField(blank=False,null=False)
   

#CLIENT LEVELS
class client_levels(models.Model):
    class Meta:
        verbose_name_plural = "client_levels"
    value = models.IntegerField(blank=False,null=False)
    

#PARTNER LEVELS
class partner_levels(models.Model):
    class Meta:
        verbose_name_plural = "partner_levels"
    value = models.IntegerField(blank=False,null=False)