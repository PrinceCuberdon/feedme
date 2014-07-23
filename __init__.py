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

from django.contrib.syndication.views import Feed
from django.conf import settings

from .models import FeedMe


def feedme(url, *args, **kwargs):
    """
    Create a feed me object (convinient function)
    @param url: The page URL
    @return: None
    """
    FeedMe.objects.create(
        title=kwargs.get('title', 'Default Title. Please Feed Me!'),
        content=kwargs.get("content", 'Default Content. Please Feed Me!'),
        url=url
    )    


class FeedGenerator(Feed):
    title = settings.FEEDME_CONFIG.Title
    link = '/'
    description = settings.FEEDME_CONFIG.Description
    
    def items(self):
        return list(FeedMe.objects.order_by('-pub_date').all()[:20])
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.content
