from django.db import models


class Population(models.Model):
    ''' The class of agriculture in marobo '''
    distrito = models.CharField(max_length=128)
    sub_distrito = models.CharField(max_length=128)
    suco = models.CharField(max_length=128)
    aldeia = models.CharField(max_length=128)

    def __unicode__(self):
        return self.suco
