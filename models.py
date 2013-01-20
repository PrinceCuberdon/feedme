# -*- coding: UTF-8 -*-
# 
# Band Cochon (c) Prince Cuberdon 2011 and Later <princecuberdon@bandcochon.fr>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
FeedMe - Django Module for feeding
"""

from django.db import models
from . import ping_all

class FeedMe(models.Model):
    """ The feed model. Store all here """ 
    creation = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    url = models.CharField(max_length=140)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return self.url
    
    class Meta:
        ordering = ('-creation', )
        

    
class PingModel(models.Model):
    """ Each model who needs to ping search engine must derivate from
    PingModel
    """
    
    def save(self, *args, **kwargs):
        """ Ping the search engines """
        ping_all()
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