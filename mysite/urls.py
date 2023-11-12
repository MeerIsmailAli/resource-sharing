from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("home/",views.index,name="home"),
    path("storage/",views.storage,name="storage"),
    path("send/",views.share_picture,name="send"),
    path("sign-up/",views.sign_up,name="sign-up"),
]
