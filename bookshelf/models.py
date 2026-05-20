from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Book(models.Model):
    STATUS_CHOICES = [
        ('TO_READ', 'To Read'),
        ('READING', 'Currently Reading'),
        ('COMPLETED', 'Finished / Completed'),
    ]

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)

    status = models.CharField(
        max_length=10, 
        choices=STATUS_CHOICES, 
        default='TO_READ'
    )

    # Rating can be empty (null=True) because "To Read" or "Reading" books aren't rated yet.
    # blank=True allows us to submit a form without a rating.
    # Validators ensure ratings are strictly between 1 and 5.
    rating = models.IntegerField(
        null=True, 
        blank=True, 
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    # 3. String representation
    def __str__(self):
        return f"{self.title} by {self.author} ({self.get_status_display()})"