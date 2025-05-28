from django.db import models

class Author(models.Model):
    authorid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    bio = models.TextField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
