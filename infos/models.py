from django.db import models

class Info(models.Model):
    """
    Info model
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    agree = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name