from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_openid$', views.get_openid),
    url(r'^test$', views.test),
    url(r'^create_user$', views.create_user),
]