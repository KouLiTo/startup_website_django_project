from django.db import models
from django.core.validators import RegexValidator



# Create your models here.

class Feedback(models.Model):
    SERVICES = (
        ("games", "Games"),
        ("consulting", "Consulting"),
        ("marketing", "Marketing of games"),
        ("licence and deploying", "Licence and Deploying"),
        ("other question", "Other question"),
    )

    name             = models.CharField(max_length=20, default="")
    surname          = models.CharField(max_length=20, default="")
    email            = models.EmailField()
    mobile           = models.CharField(max_length=15, validators=[RegexValidator(r"^[\+]\d{5,15}$")], blank=True, null=True, default="")
    subject          = models.CharField(max_length=40, choices=SERVICES)
    text             = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Projects(models.Model):
    title            = models.CharField(max_length=30)
    link             = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"