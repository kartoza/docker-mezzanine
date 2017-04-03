from account.hooks import AccountDefaultHookSet
from django.conf import settings


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
