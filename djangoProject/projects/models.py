from django.db import models, migrations
from settings.models import locations,clients,client_levels, skills, skill_levels, partners, partner_levels, weeks, availability_levels
from associates.models import associate_table


# Create your models here.


#PROJECTS
class proj_table(models.Model):
        
    name = models.CharField(max_length =50, default ='',blank=False,null=False)
    location = models.ForeignKey(locations, on_delete=models.PROTECT)
    fee = models.IntegerField(blank=False,null=False)
    team_size = models.IntegerField(blank=False,null=False)
    duration = models.IntegerField(blank=False,null=False)

 
    class Meta:
        verbose_name_plural = "project_table"
        
    def __str__(self):
        return (self.name+'('+str(self.id)+')')

    

#PROJECTS TO CLIENT MATRIX
class proj_client_relationship(models.Model):
        
    
    project_id = models.ForeignKey('proj_table', on_delete=models.CASCADE)
    client_id = models.ForeignKey(clients, on_delete=models.CASCADE)
    minimum=models.ForeignKey(client_levels, on_delete=models.CASCADE)
    isMin=models.BooleanField(default=False)
    
 
    class Meta:
        verbose_name_plural = "proj_client_relationships"
        unique_together = (("project_id", "client_id"),)
        
    def __str__(self):
        return (str(self.project_id)+' ('+str(self.client_id)+')') 
    
    
#PROJECTS TO SKILLS MATRIX
class proj_skills(models.Model):
        
    project_id = models.ForeignKey('proj_table', on_delete=models.CASCADE)
    skill_id = models.ForeignKey(skills, on_delete=models.CASCADE)
    minimum=models.ForeignKey(skill_levels, on_delete=models.CASCADE)
    isMin=models.BooleanField(default=False)    
 
    class Meta:
        verbose_name_plural = "proj_skills"
        unique_together = (("project_id", "skill_id"),)
        
    def __str__(self):
        return (str(self.project_id)+' ('+str(self.skill_id)+')')

#PROJECTS TO SKILLS MATRIX
class proj_associates(models.Model):
        
    project_id = models.ForeignKey('proj_table', on_delete=models.CASCADE)
    associate_id = models.ForeignKey(associate_table, on_delete=models.CASCADE)
    
 
    class Meta:
        verbose_name_plural = "proj_associates"
        unique_together = (("project_id", "associate_id"),)
        
    def __str__(self):
        return (str(self.project_id)+' ('+str(self.associate_id)+')')      
    
#PROJECTS  TO PARTNER MATRIX
class proj_partner_relationship(models.Model):
        
    project_id = models.ForeignKey('proj_table', on_delete=models.CASCADE)
    partner_id = models.ForeignKey(partners, on_delete=models.CASCADE)
    minimum=models.ForeignKey(partner_levels, on_delete=models.CASCADE)
    isMin=models.BooleanField(default=False)    
 
    class Meta:
        verbose_name_plural = "proj_partner_relationship"
        unique_together = (("project_id", "partner_id"),)
        
    def __str__(self):
        return (str(self.project_id)+' ('+str(self.partner_id)+')')      
