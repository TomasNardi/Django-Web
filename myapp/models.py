from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project , on_delete=models.CASCADE)
    done = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(null=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " - " + self.project.name + " - " + self.user.username + " - " + str(self.fecha)
    
    





    


