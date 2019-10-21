from django.conf.urls import url, include
from rest_framework import routers
from .api import views


router = routers.DefaultRouter()
router.register('likes', views.LikeViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
]