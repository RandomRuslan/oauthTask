from django.conf.urls import url

from vkoauth import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r"^$", views.test, name="home"),
	url(r"^login/", views.test, name="login")
]
