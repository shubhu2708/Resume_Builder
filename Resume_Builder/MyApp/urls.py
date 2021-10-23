from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
# from .views import GeneratePdf
app_name = "MyApp"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    # path("dash/", views.dash, name="index"),
    path("create_resume/", views.create_resume, name="create_resume"),
    path("srt-resume/", views.create_resume, name="srt-resume"),
    path("resume/", views.create_resume, name="resume"),





]