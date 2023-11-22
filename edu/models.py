from django.db import models


class Course(models.Model):

    title = models.CharField(max_length=150, verbose_name='название')
    preview = models.ImageField(upload_to='course/', verbose_name='превью', blank=True, null=True)
    description = models.CharField(max_length=255, verbose_name='описание')

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'

class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name='название')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')
    description = models.TextField(verbose_name='описание')
    preview_image = models.ImageField(upload_to='lesson/', verbose_name='превью', blank=True, null=True)
    video_link = models.URLField(verbose_name='ссылка на видео')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'