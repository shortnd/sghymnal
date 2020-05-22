from uuid import uuid4

from django.db.models import DateTimeField, Model, UUIDField
from simple_history.models import HistoricalRecords


class BaseModel(Model):
    uuid = UUIDField(default=uuid4, editable=False, db_index=True, unique=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        abstract = True
