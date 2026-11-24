from django.conf import settings
from django.db import models

class Student(models.Model):
    COURSE_CHOICES = [
        ("CSE", "Computer Science"),
        ("IT", "Information Technology"),
        ("ECE", "Electronics"),
        ("ME", "Mechanical"),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="students",
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    roll_number = models.CharField(max_length=30)
    course = models.CharField(max_length=10, choices=COURSE_CHOICES)
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        constraints = [
            models.UniqueConstraint(
                fields=["owner", "roll_number"],
                name="unique_roll_number_per_owner",
            ),
            models.UniqueConstraint(
                fields=["owner", "email"],
                name="unique_email_per_owner",
            ),
        ]

    def __str__(self):
        return f"{self.name} ({self.roll_number})"
