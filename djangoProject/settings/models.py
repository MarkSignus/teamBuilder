from django.db import models, migrations

# Create your models here.


#LOCATIONS
class locations(models.Model):
        
    name = models.CharField(max_length =50, default ='',blank=False,null=False)
    
 
    class Meta:
        verbose_name_plural = "locations"
        
    def __str__(self):
        return (self.name)


    
#CLIENTS
class clients(models.Model):
        
    name = models.CharField(max_length =50, default ='',blank=False,null=False)
    

    class Meta:
        verbose_name_plural = "clients"
        
    def __str__(self):
        return (self.name+'_'+str(self.id))

    
#PARTNERS  
class partners(models.Model):
        
    name = models.CharField(max_length =50, default ='',blank=False,null=False)


    class Meta:
        verbose_name_plural = "partners"
        
    def __str__(self):
        return (self.name+'_'+str(self.id))

    
    
#SKILLS  
class skills(models.Model):
        
    name = models.CharField(max_length =50, default ='',blank=False,null=False)
    
    class Meta:
        verbose_name_plural = "skills"
        
    def __str__(self):
        return self.name
    
#WEEKS  
class weeks(models.Model):
        
    number = models.IntegerField(blank=False,null=False)
    
    class Meta:
        verbose_name_plural = "weeks"
        
    def __str__(self):
        return str(self.number)
    
 #AVAILABILITY LEVELS
class availability_levels(models.Model):

    value = models.IntegerField(blank=False,null=False)
    
    class Meta:
        verbose_name_plural = "availability_levels"
        
    def __str__(self):
        return str(self.value)
    

#SKILL LEVELS
class skill_levels(models.Model):

    value = models.IntegerField(blank=False,null=False)
    
    class Meta:
        verbose_name_plural = "skill_levels"
        
    def __str__(self):
        return str(self.value)
    

   

#CLIENT LEVELS
class client_levels(models.Model):
        
    value = models.IntegerField(blank=False,null=False)
    
    class Meta:
        verbose_name_plural = "client_levels"
        
    def __str__(self):
        return str(self.value)

    

#PARTNER LEVELS
class partner_levels(models.Model):
    
    value = models.IntegerField(blank=False,null=False)
    
    class Meta:
        verbose_name_plural = "partner_levels"
        
    def __str__(self):
        return str(self.value)
    
