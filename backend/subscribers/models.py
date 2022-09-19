from django.db import models

# Create your models here
class Subscriber(models.Model):
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