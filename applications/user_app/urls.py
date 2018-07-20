from django.urls import path, include
from rest_framework import routers
from applications.user_app import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, base_name="users")

urlpatterns = [
    path(r'', include(router.urls)),
]