from django.contrib.auth import get_user_model
from django.db.models import (
    Model,
    ForeignKey,
    CharField,
    TextField,
    CASCADE,
    ImageField,
)

User = get_user_model()

class Post(Model):
    author = ForeignKey(User, on_delete=CASCADE)
    title = CharField(max_length=200)
    text = TextField()
    picture = ImageField(null=True)