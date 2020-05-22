from django.db.models import TextChoices


class Position(TextChoices):
    FORWARD = "Forward", "Forward"
    DEFENDER = "Defender", "Defender"
    MIDFIELDER = "Midfielder", "Midfielder"
    GOALKEEPER = "Goalkeeper", "Goalkeeper"
    HEAD_COACH = "Head Coach", "Head Coach"
    ASSISTANT_COACH = "Assistant Coach", "Assistant Coach"
    GOALKEEPER_COACH = "Goalkeeper Coach", "Goalkeeper Coach"
    TECHNICAL_DIRECTOR = "Technical Director", "Technical Director"
    ASSOCIATE_HEAD_COACH = "Associate Head Coach", "Associate Head Coach"
