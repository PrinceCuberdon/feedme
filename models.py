# -*- coding: UTF-8 -*-
# 
# FeedMe (c) Prince Cuberdon 2011 and Later <princecuberdon@bandcochon.fr>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is furnished
# to do so, subject to the following conditions:
#
# * The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
# * The Software is provided "as is", without warranty of any kind, express or
#   implied, including but not limited to the warranties of merchantability,
#   fitness for a particular purpose and noninfringement. In no event shall the
#   authors or copyright holders be liable for any claim, damages or other liability,
#   whether in an action of contract, tort or otherwise, arising from, out of or in
#   connection with the software or the use or other dealings in the Software.

"""
FeedMe - Django Module for feeding
"""

from django.db import models

from .pingall import ping_all


class FeedMe(models.Model):
    """ The feed model. Store all here """ 
    creation = models.DateField(auto_now=True, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    url = models.CharField(max_length=140)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return self.url
    
    class Meta:
        ordering = ('-pub_date', )
        app_label = 'feedme'


class PingModel(models.Model):
    """ Each model who needs to ping search engine must derivate from
    PingModel
    """
    
    def save(self, *args, **kwargs):
        """ Ping the search engines """
        #ping_all()
        super(PingModel, self).save(*args, **kwargs)

    class Meta:
        """ This model is totaly abstract. """
        abstract = True


class SearchEngine(models.Model):
    """ each search engine to ping are stored here """
    name = models.CharField(max_length=50)
    url = models.URLField()
    ping_count = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'feedme'
