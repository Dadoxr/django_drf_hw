from django.db import models

from users.models import User


class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name="название")
    preview = models.ImageField(
        upload_to="course/", verbose_name="превью", blank=True, null=True
    )
    description = models.CharField(max_length=255, verbose_name="описание")
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="создатель", null=True, blank=True
    )
    last_change = models.DateTimeField(auto_now=True, verbose_name='обновлен')


    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name="название")
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="курс",
        related_name="lesson",
        null=True,
        blank=True,
    )
    description = models.TextField(verbose_name="описание")
    preview_image = models.ImageField(
        upload_to="lesson/", verbose_name="превью", blank=True, null=True
    )
    video_link = models.URLField(verbose_name="ссылка на видео")
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="создатель", null=True, blank=True
    )
    last_change = models.DateTimeField(auto_now=True, verbose_name='обновлен')


    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"


class Payment(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="юзер", related_name="payment"
    )
    pay_date = models.DateTimeField(auto_now_add=True, verbose_name="дата оплаты")
    course_paid = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Оплаченый курс",
    )
    lesson_payd = models.ForeignKey(
        Lesson,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Оплаченый урок",
    )
    pay_sum = models.PositiveIntegerField(verbose_name="сумма оплаты")
    pay_method = models.CharField(
        max_length=10, choices=[("cash", "наличные"), ("transfer", "перевод на счет")]
    )

    def __str__(self):
        return f"{self.course_paid if self.course_paid else self.lesson_payd} - {self.pay_date}"

    class Meta:
        verbose_name = "оплата"
        verbose_name_plural = "оплаты"


class Subscription(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="юзер",
        related_name="subscriptions",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="курс",
        related_name="subscribed_users",
    )

    def __str__(self):
        return f"{self.user} подписан на {self.course}"

    class Meta:
        verbose_name = "подписка"
        verbose_name_plural = "подписки"
