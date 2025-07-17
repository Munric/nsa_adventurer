from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


CATEGORY_CHOICES = [
    ('adult', 'Adult'),
    ('child', 'Child'),
]

TITLE_CHOICES = [
    ('Mr', 'Mr.'),
    ('Mrs', 'Mrs.'),
    ('Ms', 'Ms.'),
    ('Dr', 'Dr.'),
]

AGE_GROUP_CHOICES = [
    ('4', '4 years'),
    ('5', '5 years'),
    ('6', '6 years'),
    ('7', '7 years'),
    ('8', '8 years'),
    ('9', '9 years'),
]

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='adult')
    detail = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        help_text="For adults: select title (Mr, Ms, etc). For children: select age group."
    )

    def __str__(self):
        return f"{self.name} ({self.category})"

