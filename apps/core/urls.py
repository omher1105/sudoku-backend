from django.conf.urls import url
from django.urls import path

from apps.core.views import create_user
from .views import current_user, UserList

urlpatterns = [
    url(r'^current_user/', current_user),
    url(r'create-user/$', create_user),
    url(r'^users/', UserList.as_view())
]
