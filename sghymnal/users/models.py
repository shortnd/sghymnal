from django.contrib.auth.models import AbstractUser
from django.db.models import BooleanField, CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    foes_allowed = BooleanField("Foes Allowed", default=False)
    push_notifications_allowed = BooleanField(
        "Push Notifications Allowed", default=False
    )
    roster_allowed = BooleanField("Rosters Allowed", default=False)
    songbook_allowed = BooleanField("Songbook Allowed", default=False)
    users_allowed = BooleanField("Users Allowed", default=False)
    feed_allowed = BooleanField("Feed Allowed", default=False)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
