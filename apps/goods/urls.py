from django.conf.urls import url
from apps.goods import views

app_name = 'goods'
urlpatterns = [
    url(r"^$", views.index, name="index")
]
