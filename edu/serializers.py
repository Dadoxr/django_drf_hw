from rest_framework import serializers

from edu.models import Course, Lesson, Payment
from users.models import User


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lesson = LessonSerializer(
        many=True,
    )

    class Meta:
        model = Course
        fields = "__all__"

    def get_lesson_count(self, course_object):
        return course_object.lesson.all().count()


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

