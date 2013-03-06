from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    main_nav = models.BooleanField()
    url_key = models.CharField(max_length=20)
    last_update = models.DateTimeField()
    """
    Symbolic links will actually link to a route and are simply for making navigation items for them dynamically
    """
    symbolic = models.TextField(default="no")

#    @classmethod
#    def __init__(self, title):
#        """ Generate our url_key on creation of content
#        Note: Known collisision issue is being ignored for small scale app
#        """
#        self.title = title
#
#        # get rid of those spaces
#        t = '-'.join(self.title.split())
#        # remove the punctuation
#        u = ''.join([c for c in t if c.isalnum() or c=='-'])
#        self.url_key = u[:20].rstrip('-').lower()

class News(models.Model):
    posted = models.DateTimeField()
    body = models.TextField()
    