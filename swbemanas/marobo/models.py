from django.db import models


class Population(models.Model):
    ''' The class of agriculture in marobo '''
    distrito = models.CharField(max_length=128)
    sub_distrito = models.CharField(max_length=128)
    suco = models.CharField(max_length=128)
    aldeia = models.CharField(max_length=128)

    def __unicode__(self):
        return self.suco


class Suco(models.Model):
    ''' The class of agriculture in marobo '''
    name = models.CharField(max_length=128)
    descriptions = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Aldeia(models.Model):
    ''' The class of agriculture in marobo '''
    name = models.CharField(max_length=128)
    populations = models.CharField(max_length=128)
    suco = models.ForeignKey(Suco, blank=False, null=False)
    descriptions = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name
