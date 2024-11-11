from django.db import models

class User(models.Model):
    user_nickname = models.CharField(primary_key=True, max_length=100, default='')
    user_name = models.CharField(max_length=150, default='')
    user_email = models.EmailField(default='')
    user_age = models.IntegerField(default=0)

    def __str__(self):
        return f'Nickname: {self.user_nickname} | Email: {self.user_email}'
    
class UserTask(models.Model):
    user_nickname = models.CharField(max_length=100, default='')
    user_task = models.CharField(max_length=500, default='')

    def __str__(self):
        return f'Nickname: {self.user_nickname} | Task: {self.user_task}'