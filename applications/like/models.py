from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class Like(models.Model):
    content_type = models.ForeignKey(ContentType,
                                     verbose_name=_('content type'),
                                     related_name="content_type_set_for_%(class)s",
                                     on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name="liking", on_delete=models.CASCADE)

    content_object = GenericForeignKey(
        ct_field="content_type",
        fk_field="object_id"
    )

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ("user", "content_type", "object_id"),
        )

    def __str__(self):
        return "{0} likes {1}".format(self.user, self.content_object)
