from rest_framework import serializers

from edu.models import Course, Lesson, Payment, Subscription
from edu.validators import LessonVideoLinkValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LessonVideoLinkValidator(field="video_link")]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lesson = LessonSerializer(many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = [
            "pk",
            "id",
            "title",
            "preview",
            "description",
            "owner",
            "lesson_count",
            "lesson",
            "is_subscribed",
        ]

    def get_lesson_count(self, course_object):
        return course_object.lesson.all().count()

    def get_is_subscribed(self, obj):
        user = self.context["request"].user
        return Subscription.objects.filter(user=user, course=obj)


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
