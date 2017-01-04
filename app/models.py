from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=255, unique=True)
    job_position = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    hours_per_week = models.IntegerField()
    where_found_us = models.CharField(max_length=200)
    country = models.CharField(max_length=50)
    english_level = models.CharField(max_length=50)
    comments = models.CharField(max_length=255)

    def __str__(self):
        return self.name
