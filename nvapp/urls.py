from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path("career/", views.career, name="career"),
    path("jobs/", views.jobs, name="jobs"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("logout/", views.logout, name="logout"),
    path("python_application/",views.python_application, name="python_application"),
    path("java_application/",views.java_application, name="java_application"),
    path("ass_application/",views.ass_application, name="ass_application"),
    path("coordinator_application/",views.coordinator_application, name="coordinator_application"),
    path("java_full_application/",views.java_full_application, name="java_full_application"),
    path("python_full_application/",views.python_full_application, name="python_full_application"),
    path("success_page/", views.success_page, name="success_page"),
]



