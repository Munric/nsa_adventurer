from django.db import models
from django.core.exceptions import ValidationError

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

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Attendee(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='adult')
    detail = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        help_text="For adults: select title (Mr, Ms, etc). For children: select age group."
    )

    def clean(self):
        # Ensure the 'detail' matches the 'category'
        if self.category == 'adult' and self.detail not in dict(TITLE_CHOICES):
            raise ValidationError({'detail': 'Invalid title for adult category.'})
        elif self.category == 'child' and self.detail not in dict(AGE_GROUP_CHOICES):
            raise ValidationError({'detail': 'Invalid age group for child category.'})

    def __str__(self):
        return f"{self.name} ({self.category})"
