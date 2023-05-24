from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Category, Comment, Course, Lesson


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title", "slug")


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "title", "slug", "short_description", "get_image")


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id", "title", "slug", "long_description", "get_image")


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            "id",
            "title",
            "slug",
            "lesson_type",
            "short_description",
            "long_description",
        )


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "name", "content", "created_at")
