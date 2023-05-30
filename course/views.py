from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Comment, Course, Lesson
from .serializers import (
    CommentsSerializer,
    CourseDetailSerializer,
    CourseListSerializer,
    LessonListSerializer,
    UserSerializer,
)


@api_view(["GET"])
def get_courses(request):
    category_id = request.GET.get("category_id", "")
    courses = Course.objects.filter(status=Course.PUBLISHED)

    if category_id:
        courses = courses.filter(categories__in=[int(category_id)])

    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_course(request, slug):
    course = Course.objects.get(slug=slug)
    serializer = CourseDetailSerializer(course)
    return Response(serializer.data)


@api_view(["GET"])
def get_author_courses(request, user_id):
    user = User.objects.get(pk=user_id)
    courses = user.courses.filter(status=Course.PUBLISHED)

    user_serializer = UserSerializer(user, many=False)
    courses_serializer = CourseListSerializer(courses, many=True)

    return Response(
        {"courses": courses_serializer.data, "created_by": user_serializer.data}
    )


@api_view(["GET"])
def get_course(request, slug):
    course = Course.objects.filter(status=Course.PUBLISHED).get(slug=slug)
    course_serializer = CourseDetailSerializer(course)
    lesson_serializer = LessonListSerializer(course.lessons.all(), many=True)

    return Response(
        {"course": course_serializer.data, "lessons": lesson_serializer.data}
    )


@api_view(["POST"])
def add_comment(request, course_slug, lesson_slug):
    data = request.data
    print(data)
    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.get(slug=lesson_slug)

    comment = Comment.objects.create(
        course=course,
        lesson=lesson,
        name=data.get("name"),
        content=data.get("content"),
        created_by=request.user,
    )

    serializer = CommentsSerializer(comment)
    print(serializer.data)

    return Response(serializer.data)


@api_view(['GET'])
def get_comments(request, course_slug, lesson_slug):
    lesson = Lesson.objects.get(slug=lesson_slug)
    serializer = CommentsSerializer(lesson.comments.all(), many=True)
    return Response(serializer.data)
