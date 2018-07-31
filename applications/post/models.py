from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from common.base_models import AbstractBaseModel
from .managers import PostManager


class Post(AbstractBaseModel):
    """
    Records posts from user
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=_('User'), related_name="user_posts",
        on_delete=models.CASCADE, )
    text = models.TextField(_("Text"))
    blocked = models.BooleanField(default=False, verbose_name=_('Blocked'))

    objects = PostManager()

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ['-created']

    def __str__(self):
        return "'%s' by %s" % (self.text[20:], self.user.get_username())

