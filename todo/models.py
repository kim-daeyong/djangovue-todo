from django.db import models

 #Create your models here.

class Todo(models.Model):
 name = models.CharField('NAMW', max_length=5, blank=True)
 todo = models.CharField('TODO', max_length=50)


 #스트링 메소드
 def __str__(self):
  return self.todo

 #admin에서도 볼 수 있게 등록해줘야 한다. admin.py에

 def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
  if not self.name:
   self.name = 'test'
   super().save()