from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    """Model for a Note."""
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    def __str___(self):
        """Return the title of the note."""
        return self.title


class Player(models.Model):
    playerID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    school = models.CharField(max_length=120)
    noted = models.ForeignKey(Note,
                              blank=True,
                              null=True,
                              on_delete=models.CASCADE,
                              related_name='players')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"