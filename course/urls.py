from django.urls import path

from course import views

urlpatterns = [
    path("", views.get_courses),
    path("get_author_courses/<int:user_id>/", views.get_author_courses),
]
