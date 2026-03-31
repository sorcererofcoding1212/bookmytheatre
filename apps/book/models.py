from django.db import models

# Create your models here.

class Book(models.Model):
    user = models.ForeignKey(to='users.Account', on_delete=models.CASCADE)
    show = models.ForeignKey(to='shows.Show', on_delete=models.RESTRICT)
    booking_at = models.DateTimeField(auto_now_add=True, blank=True)
    ticket_quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.user}:{self.show}'