from account.hooks import AccountDefaultHookSet
from django.core.mail import send_mail
from django.template.loader import render_to_string
from account.conf import settings


class PinaxAccountHookset(AccountDefaultHookSet):

    """Overriding Send Password Email"""
    def send_password_reset_email(self, to, ctx):
        key = ctx["password_reset_url"].rstrip('/').rsplit('/', 1)[-1]
        newcontext = {
            "current_site": ctx["current_site"],
            "user": ctx["user"],
            "password_reset_url": ctx["password_reset_url"],
            "key": key,
            "host": settings.CONFERENCE_DOMAIN
        }
        super(PinaxAccountHookset,self).send_password_reset_email(to, newcontext)

    def send_complete_profile_email(self,to,ctx):
        subject = render_to_string("account/email/email_complete_profile_subject.txt",ctx)
        subject = "".join(subject.splitlines())  # remove superfluous line breaks
        message = render_to_string("account/email/email_complete_profile_message.txt", ctx)
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, to)
