feedme
======

Django automatic RSS/ATOM builder. Also a multiple web search engine pinger


Installation
------------

After forking or downloading add "feedme" in the Django INSTALLED_APPS list in settings file. 
Then launch manage.py syncdb in a shell to create needed tables.

Still in the settings.py file create a class called FEEDME_CONFIG which contains two fields: Title and Description (see above)

```python
class FEEDME_CONFIG:
    Title = "This is a demo"
    Description = "Every body enjoy demos"
```


