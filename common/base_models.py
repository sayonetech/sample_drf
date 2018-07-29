from django.db import models
from django.utils.translation import ugettext_lazy as _


class AbstractBaseModel(models.Model):

    """
    Base model for all others
    """

    created = models.DateTimeField(_("Created Time"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified Time"), auto_now=True)

    class Meta:
        abstract = True