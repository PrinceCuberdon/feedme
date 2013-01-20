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


