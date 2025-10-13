from django.db import models

class Enquiry(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Replied', 'Replied'),
        ('Closed', 'Closed'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    project_type = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
