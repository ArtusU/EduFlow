from django.urls import path

from course import views

urlpatterns = [
    path("", views.get_courses),
    path("<slug:slug>/", views.get_course),
    path("get_author_courses/<int:user_id>/", views.get_author_courses),
    path('<slug:course_slug>/<slug:lesson_slug>/', views.add_comment),
]
