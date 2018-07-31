from django.db import models
from django.utils.translation import ugettext_lazy as _


class CreateBaseModel(models.Model):
    """
    Model that can inherit for models with create field
    """
    created = models.DateTimeField(_("Created Time"), auto_now_add=True)

    class Meta:
        abstract = True


class AbstractBaseModel(CreateBaseModel):

    """
    Base model for all others, included modified datetime field
    """
    modified = models.DateTimeField(_("Modified Time"), auto_now=True)

    class Meta:
        abstract = True