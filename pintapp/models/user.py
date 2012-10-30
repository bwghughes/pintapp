from datetime import datetime
from dictshield.document import Document
from dictshield.fields import (StringField, IntField, UUIDField, DateTimeField, BooleanField)


class User(Document):
    guid = UUIDField(auto_fill=True)
    name = StringField()
    mobile_number = StringField()
    verified = BooleanField(default=False)
    token = IntField()
    created_at = DateTimeField(default=datetime.now)
