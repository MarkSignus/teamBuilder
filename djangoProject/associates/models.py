from django.db import models, migrations
from settings.models import locations,clients,client_levels, skills, skill_levels, partners, partner_levels, weeks, availability_levels

# Create your models here.


#ASSOCIATES
class associate_table(models.Model):
        
    name = models.CharField(max_length =50, default ='',blank=False,null=False)
    location = models.ForeignKey(locations, on_delete=models.PROTECT)
    rate = models.IntegerField(blank=False,null=False)

 
    class Meta:
        verbose_name_plural = "associate_table"
        
    def __str__(self):
        return self.name+'_'+str(self.id)

    

#ASSOC TO CLIENT MATRIX
class assoc_client_relationship(models.Model):
        
    
    associate_id = models.ForeignKey('associate_table', on_delete=models.PROTECT)
    client_id = models.ForeignKey(clients, on_delete=models.PROTECT)
    level=models.ForeignKey(client_levels, on_delete=models.PROTECT)
    
 
    class Meta:
        verbose_name_plural = "assoc_client_relationships"
        unique_together = (("associate_id", "client_id"),)
        
    def __str__(self):
        return str(self.associate_id)+'_'+str(self.client_id) 
    
    
#ASSOC TO SKILLS MATRIX
class assoc_skills(models.Model):
        
    associate_id = models.ForeignKey('associate_table', on_delete=models.PROTECT)
    skill_id = models.ForeignKey(skills, on_delete=models.PROTECT)
    level=models.ForeignKey(skill_levels, on_delete=models.PROTECT)
    
 
    class Meta:
        verbose_name_plural = "assoc_skills"
        unique_together = (("associate_id", "skill_id"),)
        
    def __str__(self):
        return str(self.associate_id)+'_'+str(self.skill_id)

#ASSOC TO SKILLS MATRIX
class assoc_availability(models.Model):
        
    associate_id = models.ForeignKey('associate_table', on_delete=models.PROTECT)
    week_id = models.ForeignKey(weeks, on_delete=models.PROTECT)
    level=models.ForeignKey(availability_levels, on_delete=models.PROTECT)
    
 
    class Meta:
        verbose_name_plural = "assoc_availabilities"
        unique_together = (("associate_id", "week_id"),)
        
    def __str__(self):
        return str(self.associate_id)+'_'+str(self.week_id)       
    
#ASSOC TO PARTNER MATRIX
class assoc_partner_relationship(models.Model):
        
    associate_id = models.ForeignKey('associate_table', on_delete=models.PROTECT)
    partner_id = models.ForeignKey(partners, on_delete=models.PROTECT)
    level=models.ForeignKey(partner_levels, on_delete=models.PROTECT)
    
 
    class Meta:
        verbose_name_plural = "assoc_partner_relationships"
        unique_together = (("associate_id", "partner_id"),)
        
    def __str__(self):
        return str(self.associate_id)+'_'+str(self.partner_id)     
