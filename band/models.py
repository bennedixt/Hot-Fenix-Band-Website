from django.db import models

class BandMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='members/')  # Optional for pictures of band members

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='albums/')
    description = models.TextField()

    def __str__(self):
        return self.title

class Concert(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.location} on {self.date}"
