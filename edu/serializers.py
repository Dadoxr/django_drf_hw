from rest_framework import serializers

from edu.models import Course, Lesson


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(read_only=True)
    lesson = LessonListSerializer(many=True,)

    class Meta:
        model = Course
        fields = '__all__'
    
    def get_lesson_count(self, course_object):
        return course_object.lesson.all().count()


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'