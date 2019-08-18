from django.db import models

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class SuperHero(models.Model):
    name = models.CharField(max_length=30, unique=True)
    biography = models.TextField()
    publisher = models.ManyToManyField(Publisher)
    alter_ego = models.CharField(max_length=30)
    superpowers = models.TextField()
    team_affiliation = models.ManyToManyField(Team)

    def __str__(self):
        return self.name
