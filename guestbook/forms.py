from django.forms import ModelForm
from guestbook.models import Message

class GuestbookForm(ModelForm):
    class Meta:
        model = Message
