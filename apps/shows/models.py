from django.db import models

# Create your models here.


class Venue(models.Model):
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=200, blank=True)
    city = models.ForeignKey(
        to='users.City', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Screen(models.Model):
    venue = models.ForeignKey(to=Venue, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    capacity = models.PositiveIntegerField(default=150)

    def __str__(self):
        return f'{self.name}: {self.venue}'


class Show(models.Model):
    movie = models.ForeignKey(to='movies.Movie', on_delete=models.CASCADE)
    screen = models.ForeignKey(to=Screen, on_delete=models.CASCADE)
    show_timings = models.DateTimeField()
    ticket_price = models.PositiveIntegerField(default=250)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['screen', 'show_timings'], name='unique_show')
        ]

    def __str__(self):
        return f'{self.screen}: {self.movie}: {self.show_timings}'
