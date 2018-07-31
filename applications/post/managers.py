from django.db import models


class PostManager(models.Manager):
    def public(self):
        """
        QuerySet for all posts available to public
        """
        return self.get_queryset().filter(blocked=False)