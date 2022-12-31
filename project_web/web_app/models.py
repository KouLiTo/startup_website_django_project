from django.db import models
from django.core.validators import RegexValidator



# Create your models here.

class Feedback(models.Model):
    SERVICES = (
        ("games", "Games"),
        ("consulting", "Consulting"),
        ("marketing", "Marketing of games"),
        ("licence and deploying", "Licence and Deploying"),
        ("technical question", "Technical Question"),
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


class Basic(models.Model):
    deploy_to_the_store           = models.BooleanField(default=False)
    design                        = models.BooleanField(default=False)
    animation                     = models.BooleanField(default=False)
    source_code                   = models.BooleanField(default=False)
    marketing_consulting          = models.BooleanField(default=False)
    number_of_levels              = models.PositiveSmallIntegerField()
    awaiting_time                 = models.PositiveSmallIntegerField()
    price                         = models.FloatField()




class Standard(models.Model):
    deploy_to_the_store            = models.BooleanField(default=False)
    design                         = models.BooleanField(default=False)
    animation                      = models.BooleanField(default=False)
    source_code                    = models.BooleanField(default=False)
    marketing_consulting           = models.BooleanField(default=False)
    number_of_levels               = models.PositiveSmallIntegerField()
    awaiting_time                  = models.PositiveSmallIntegerField()
    price                          = models.FloatField()




class Premium(models.Model):
    deploy_to_the_store            = models.BooleanField(default=False)
    design                         = models.BooleanField(default=False)
    animation                      = models.BooleanField(default=False)
    source_code                    = models.BooleanField(default=False)
    marketing_consulting           = models.BooleanField(default=False)
    number_of_levels               = models.PositiveSmallIntegerField()
    awaiting_time                  = models.PositiveSmallIntegerField()
    price                          = models.FloatField()


