from django.conf.urls import url, include
from rest_framework import routers
from .api import views as v1_views


router = routers.DefaultRouter()
router.register('posts', v1_views.PostViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]