from django.views.generic import TemplateView
from django.db import models


class Potential(models.Model):
    ''' The class of agriculture in marobo '''
    name = models.CharField(max_length=128, help_text=_('the name of the potential')
    location = models.CharField(max_length=128, help_text=_('the location of the potential')
    image = models.ImageField(null=True blank=True)

    def __unicode__(self):
        return self.name
