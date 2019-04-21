from django.conf.urls import url
from apps.user import views

app_name = "user"
urlpatterns = [
    url(r"^register$", views.register, name="register"),
    url(r"^register_handler$", views.register_handler, name="register_handler"),
]