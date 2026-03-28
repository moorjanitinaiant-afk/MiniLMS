from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings


@receiver(user_logged_in)
def send_login_email(sender, request, user, **kwargs):
    if user.email:
        send_mail(
            subject="Login Successful - BCA LMS Portal",
            message=(
                f"Hello {user.username},\n\n"
                "You have successfully logged in to BCA LMS Portal.\n\n"
                "Regards,\nBCA LMS Team"
            ),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
