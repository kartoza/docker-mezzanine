from account.signals import email_confirmed
from django.dispatch import receiver
import logging
from account.hooks import hookset
import re


@receiver(email_confirmed)
def email_confirmed_callback(sender, **kwargs):
    accounts_data = kwargs.get("email_address","failed").split()
    if len(accounts_data) > 1:
        email_address = accounts_data[0]
        username = re.sub('()','',accounts_data[1])
        ctx = {
            "email_address": email_address,
            "username":username
        }
        hookset.send_complete_profile_email(email_address,ctx)