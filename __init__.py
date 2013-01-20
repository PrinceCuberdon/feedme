# -*- coding: UTF-8 -*-
# 
# FeedMe (c) Prince Cuberdon 2011 and Later <princecuberdon@bandcochon.fr>
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
FeedMe - Feed Generator
"""

import datetime
import threading

from django.contrib.syndication.views import Feed
from django.conf import settings

def feedme(url, *args, **kwargs):
    from .models import FeedMe
    FeedMe.objects.create(
         creation = datetime.datetime.now(),
         title = kwargs.get('title', 'Default Title. Please Feed Me!'),
         content = kwargs.get("content", 'Default Content. Please Feed Me!'),
         url = url
    )    
    
class FeedGenerator(Feed):
    title = settings.FEEDME_CONFIG.Title
    link = '/'
    description = settings.FEEDME_CONFIG.Description
    
    def items(self):
        return FeedMe.objects.all()[:20]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.content


def ping_all():
    """
    Pings the popular search engines, Google, Yahoo, ASK, and
    Bing, to let them know that you have updated your
    site's sitemap. Returns successfully pinged servers.

    We start a thread because ping_google is blocking the main thread.
    """
    from django.contrib.sitemaps import ping_google
    from django.contrib.sites.models import Site
    from .models import SearchEngine

    sitemap_url = "http://%s/sitemap.xml" % Site.objects.get_current().domain

    def pa():
        engines = SearchEngine.objects.filter(active=True).only('name', 'url')
        
        for engine in list(engines):
            try:
                ping_google(sitemap_url=sitemap_url, ping_url=engine.url)
                pinged = True
            except:
                # Don't care about errors. Just notice it
                pinged = False
            
            if pinged:
                engine.ping_count += 1
                engine.save()
        
    threading.Thread(target=pa).start()


