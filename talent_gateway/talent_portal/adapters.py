from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import redirect
from allauth.exceptions import ImmediateHttpResponse
from allauth.utils import get_user_model
from allauth.account.utils import perform_login
from django.conf import settings
import logging
from allauth.account.adapter import DefaultAccountAdapter

logger = logging.getLogger(__name__)


# TODO: complete the docstring
class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    """
    Converting the username to email
    """
    def pre_social_login(self, request, sociallogin):
        email_address = sociallogin.account.extra_data['email']
        user = get_user_model()
        users = user.objects.filter(email=email_address)
        if users:
            # allauth.account.app_settings.EmailVerificationMethod
            perform_login(request, users[0], email_verification='optional')
            raise ImmediateHttpResponse(
                    redirect(settings.LOGIN_REDIRECT_URL.format(id=request.user.id)))

        # we are keeping the username same as the email address of the user.
        sociallogin.user.username = email_address


# TODO: complete the docstring
class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
            Saves a new `User` instance using information provided in the
            signup form.
            """
        from allauth.account.utils import user_username, user_email, user_field

        data = form.cleaned_data
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')

        # setting the username as the email so that it is used.
        # username = data.get('username')  # all-auth code
        username = email  # using the email as the username

        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, 'first_name', first_name)
        if last_name:
            user_field(user, 'last_name', last_name)
        if 'password1' in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user
