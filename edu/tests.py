from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from edu.models import Course, Lesson, Subscription
from users.models import User


class LessonAPITestCase(TestCase):
    def setUp(self):
        self.title = "test title"
        self.correct_title = "test correct title"
        self.description = "test description"
        self.incorrect_video_link = "https://not_youtube.com/jhijk"
        self.correct_video_link = "https://youtube.com/jkjk"

    def test_create_lesson(self):
        data = {
            "title": self.title,
            "description": self.description,
            "video_link": self.correct_video_link,
        }

        response = self.client.post(reverse("edu:lesson_create"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Lesson.objects.all().exists())
        self.assertEqual(
            response.json(),
            {
                "id": 1,
                "title": self.title,
                "description": self.description,
                "preview_image": None,
                "video_link": self.correct_video_link,
                "course": None,
                "owner": None,
            },
        )

    def test_create_lesson_bad_request(self):
        data = {
            "title": self.title,
            "description": self.description,
            "video_link": self.incorrect_video_link,
        }

        response = self.client.post(reverse("edu:lesson_create"), data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_lesson_list(self):
        response = self.client.get(reverse("edu:lesson_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_lesson(self):
        data = {
            "title": self.title,
            "description": self.description,
            "video_link": self.correct_video_link,
        }
        lesson = Lesson.objects.create(**data)

        response = self.client.get(reverse("edu:lesson_get", kwargs={"pk": lesson.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_lesson(self):
        data = {
            "title": self.title,
            "description": self.description,
            "video_link": self.correct_video_link,
        }
        lesson = Lesson.objects.create(**data)
        correct_data = {
            "title": self.correct_title,
            "description": self.description,
            "video_link": self.correct_video_link,
        }

        response = self.client.put(
            reverse("edu:lesson_update", kwargs={"pk": lesson.pk}),
            data=correct_data,
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json().get("title"),
            self.correct_title,
        )

    def test_delete_lesson(self):
        data = {
            "title": self.title,
            "description": self.description,
            "video_link": self.correct_video_link,
        }
        lesson = Lesson.objects.create(**data)

        response = self.client.delete(
            reverse("edu:lesson_delete", kwargs={"pk": lesson.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SubscriptionAPITestCase(TestCase):
    def setUp(self):
        email = "user@user.user"
        password = "user"
        self.user = User.objects.create(email=email, password=password)

        title = "test title"
        description = "test description"
        self.course = Course.objects.create(title=title, description=description)

    def test_post_subscription(self):
        response = self.client.post(
            reverse(
                "edu:subscribe_course",
                kwargs={"user_pk": self.user.pk, "course_pk": self.course.pk},
            )
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(), {"detail": "Подписка успешно установлена"})

        response = self.client.post(
            reverse(
                "edu:subscribe_course",
                kwargs={"user_pk": self.user.pk, "course_pk": self.course.pk},
            )
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"detail": "Вы уже подписаны на этот курс"})

    def test_delete_subscription(self):
        response = self.client.delete(
            reverse(
                "edu:unsubscribe_course",
                kwargs={"user_pk": self.user.pk, "course_pk": self.course.pk},
            )
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), {"detail": "Вы не подписаны на этот курс"})
        a = Subscription.objects.create(user=self.user, course=self.course)

        response = self.client.delete(
            reverse(
                "edu:unsubscribe_course",
                kwargs={"user_pk": self.user.pk, "course_pk": self.course.pk},
            )
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
