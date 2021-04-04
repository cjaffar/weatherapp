from django.db                      import models
from django.utils                   import timezone

class ActiveOnly(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)

class City(models.Model) :

    cityid = models.IntegerField(unique=True)
    name = models.CharField(max_length=42)
    country = models.CharField(max_length=2)
    coord = models.JSONField()
    status = models.BooleanField(default=True, blank=True)

    ##in a larger project, can put these in own class and inherit from it.
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    active = ActiveOnly()

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name

class Weather(models.Model) :

    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now())
    ###float fields since we are storing smaller values.
    min_temp = models.FloatField(default=0.0)
    max_temp = models.FloatField(default=0.0)
    wind_speed = models.FloatField(default=0.0)
    weather = models.JSONField()
    rain = models.CharField(max_length=32)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('city',)
        unique_together=['city','date']

    def __str__(self):
        return self.city.name