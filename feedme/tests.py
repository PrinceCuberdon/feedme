# -*- coding: UTF-8 -*-
"""
Test file for FeedMe application.

"""

from django.test import TestCase

from feedme import feedme
from feedme.models import FeedMe

class FeedMeTest(TestCase):
    def test_feed_me(self):
        feedme('/', title="Test", content="Test Me")
        self.assertEqual(FeedMe.objects.all().count(), 1)
    
    def test_feedme_rss(self):
        """ Don't know how to do """
