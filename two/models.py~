from django.db import models

# Create your models here.
class Choice(models.Model):
    #first_name= models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #id_num = models.IntegerField(default=1)
    #number = models.IntegerField(default=0)
    
class Position(models.Model):
    position = models.ForeignKey(Choice)
    #choice = models.CharField(max_length=200)
    #votes = models.IntegerField(default=0)
    #number = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

    
class Poll(models.Model):
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'
