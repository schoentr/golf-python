from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
  """
  This is where course specific infomation is stored, 
  """
  name = models.CharField(max_length=200)
  street = models.CharField(max_length=100, blank=True)
  city = models.CharField(max_length=50)
  region = models.CharField(max_length=20)
  zip_Code = models.CharField(max_length=20, blank=True)
  date_added = models.DateField(auto_now=True)

   
  def __repr__(self):
    return f'<Course: {  self.name } | Date: {self.date_added}>'
  
  def __str__(self):
    return f'{  self.name }'

class Tee(models.Model):
  """
  This table is where tee specific slope and rating information is stored to calculate, the users differectial. 

  It depends on Courses,  and  Rounds depend on it.
  """
  course = models.ForeignKey(Course, on_delete=models.CASCADE)
  color = models.CharField(max_length=20)
  length = models.CharField(max_length=20, default="- yards")
  rating = models.DecimalField(max_digits=5,decimal_places=2, blank=True)
  slope = models.IntegerField()
  par = models.IntegerField(default=72)
  date_added = models.DateField(auto_now=True)



  def __repr__(self):
    return f'< {self.color}>'
  def __str__(self):
    return f'{self.course} -- {self.color}'

class Round(models.Model):
  """
  This table is where users add there score and date played, It is dependent on the user selecting the  course and tee, the defferential will be calculated based on the user's score and the tee's slope and rating.

  Depends on Courses, Tees

  """
  user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_name')
  tee = models.ForeignKey(Tee, on_delete=models.CASCADE)
  score= models.IntegerField()
  differential=models.DecimalField(max_digits=5,decimal_places=2, blank=True)
  date_played=models.DateField(blank=True)
  used = models.BooleanField(default=False)
 
  def __repr__(self):
    return f'<Score:{self.score}>'
  def __str__(self):
    return f'User:{self.user} |  Tee:{self.tee}|   Score:{self.score}'




# Create your models