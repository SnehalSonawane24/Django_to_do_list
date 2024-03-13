from django.db import models
# built-in user model, user model take care of user authentication
from django.contrib.auth.models import User
# Create your models here.
# inherites Model from models
class Task(models.Model):
    # user = models.CharField(max_length = 200)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length = 200)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    created = models.DateField(auto_now_add = True)
    # update = models.CharField(max_length = 200)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering =['complete']
