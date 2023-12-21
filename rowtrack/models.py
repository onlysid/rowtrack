from django.db import models

# Create your models here.
class RowMachine(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    def __str__(self):
        return self.name
    
class MachineMessage(models.Model):
    row_machine = models.ForeignKey(RowMachine, on_delete=models.CASCADE)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-time']