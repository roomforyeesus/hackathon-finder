from django.db import models

# Create your models here
class Subscribers(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    email = models.EmailField()
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name + ' ' + self.email
    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'
    
class Contests(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=128)
    start_time = models.CharField(max_length=128)
    end_time = models.CharField(max_length=128)
    duration = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    in_24_hours = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name + ' ' + self.url
    class Meta:
        verbose_name = 'Contest'
        verbose_name_plural = 'Contests'