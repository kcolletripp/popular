from __future__ import unicode_literals

from django.db import models

class Target(models.Model):
    target_name = models.CharField(max_length=200)
    wiki_views = models.IntegerField(default=0)
    def __str__(self):
        return self.target_name

#class TargetWiki(models.Model):
#    target = models.ForeignKey(Target, on_delete=models.CASCADE)
#    wiki_name = models.CharField(max_length=200)
#    wiki_hits = models.IntegerField(default=0)
#    def __str__(self):
#        name = "Name: " + self.wiki_name + "Hits: " + str(self.wiki_hits)
#        return name
