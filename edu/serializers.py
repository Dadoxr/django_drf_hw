from rest_framework import serializers

from edu.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Course
        fields = '__all__'
    
    def get_lesson_count(self, lesson_object):
        return lesson_object.lesson_set.all().count()


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'