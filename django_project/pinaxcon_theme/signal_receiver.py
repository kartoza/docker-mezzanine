from account.signals import email_confirmed
from django.dispatch import receiver
from account.conf import settings
from account.hooks import hookset
from account.models import EmailAddress
import re


@receiver(email_confirmed)
def email_confirmed_callback(sender, **kwargs):
    email = kwargs.get("email_address")
    email_address = email.email
    username = email.user.username
    ctx = {
        "host": settings.CONFERENCE_DOMAIN,
        "email_address": email_address,
        "username": username
    }
    hookset.send_complete_profile_email([email_address], ctx)

