FeedMe
======

Django automatic RSS/ATOM builder. Also a multiple web search engine pinger. This package is designed to
run with the http://www.bandcochon.re web site, so, there's not `setup.py` file to build the package.

Installation
------------

After forking or downloading add "feedme" in the Django `INSTALLED_APPS` list in settings file. 
Then launch manage.py syncdb in a shell to create needed tables.

Still in the `settings.py` file create a class called `FEEDME_CONFIG` which contains two fields: Title and Description (see above)

```python
class FEEDME_CONFIG:
    Title = "This is a demo"
    Description = "Every body enjoy demos"
```

Then you must sychronize the database with `./manage.py syncdb` to create the missing tables.

Go the the /admin/feedme/ and first, set the SearchEngines. I recommand you to ping :

* Google
* Bing
* Yahoo!

Then in your `urls.py` project file add :

```python
from feedme import FeedGenerator

urlpatterns = patterns('',
    # Urls here
    url(r'^rss/$', FeedGenerator(), name="rss"),
    # Other urls here
)
```

Do not forget to create the `sitemap.xml` file using the SiteMap framework (https://docs.djangoproject.com/en/dev/ref/contrib/sitemaps/)


That's it! FeedMe is ready to be feeded.

Using automatic ping
--------------------

Using FeedMe is very easy. Each time you need to ping a search engine, you derivate from `PingModel` your
model class.

For a blog it may be like this:

```python
from feedme import PingModel

class Post(PingModel):
    ''' This is my blog post ''''
    # Your fields here
```

Each time a Post entry have been added or modified, each search engine are pinged.

Note: The search engines ping is encapsuled in a python thread, so it is non blocking.

Using FeedMe
------------

To fill your RSS/ATOM feeds use the convinient function `feedme`

```python
from feedme import feedme

class Post(PingModel):
    # Stuffes here
    def save(self, \*args, \*\*kwargs):
        """ Save your feed """
        feedme(self.get_absolute_url(), # The source URL. The user go there form its feed reader
               title=self.title,        # title: The feed item title.
                                        #   The default is "Default Title. Please Feed Me!"
               content=self.content)    # content: The feed content (may be in HTML).
                                        #   The default content is : "Default Content. Please Feed Me!"
```

That's all.


