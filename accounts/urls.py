from django.urls import path
from . import views
urlpatterns=[
    path("", views.index, name="index"),
    path("signin", views.signin, name="signin"),
    path("login", views.login_user, name="Login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("logout", views.logout_user, name="logout"),
    path("postblog", views.create_blog, name="create_blog"),
    path("readpost", views.readpost, name="readPost"),
    path("myuploads", views.myuploads, name="myuploads")
]