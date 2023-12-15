import re
from typing import Any

from rest_framework.exceptions import ValidationError


class LessonVideoLinkValidator:
    def __init__(self, field) -> None:
        self.field = field

    def __call__(self, ordered_dict) -> Any:
        reg = re.compile(r"https?://(?:www\.)?youtube\.com/")
        video_link = dict(ordered_dict).get(self.field)

        if not bool(reg.match(video_link)):
            raise ValidationError("Ссылка должна быть только на YouTube")
