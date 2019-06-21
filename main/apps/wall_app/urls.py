from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.root),
    url(r'^wall$', views.wall),
    url(r'^post_message$', views.post_message), # /post_message

    # Register and Login
    url(r'^users/reg_login', views.reg_login),
    url(r'^users/reg', views.register),
    url(r'^users/userLogin', views.userLogin),
    url(r'^users/logout', views.logout),
    #url(r'^users/adminLogin', views.adminLogin),
]
