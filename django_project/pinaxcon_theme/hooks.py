from account.hooks import AccountDefaultHookSet
from django.core.mail import send_mail
from django.template.loader import render_to_string
from account.conf import settings


class Foss4GAccountHookset(AccountDefaultHookSet):
    def send_invitation_email(self, to, ctx):
        subject = render_to_string("account/email/email_confirmation_subject.txt", ctx)
        subject = "".join(subject.splitlines())  # remove superfluous line breaks
        message = render_to_string("account/email/email_confirmation_message.txt", ctx)
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, to)

    def send_complete_profile_email(self,to,ctx):
        subject = render_to_string("account/email/email_complete_profile_subject.txt",ctx)
        subject = "".join(subject.splitlines())  # remove superfluous line breaks
        message = render_to_string("account/email/email_complete_profile_message.txt", ctx)
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, to)
