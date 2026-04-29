from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Ad
from django.core.mail import send_mail
from django.conf import settings


@receiver(post_save, sender=Ad)
def check_ad_expiration(sender, instance, created, **kwargs):
    if not created:
        instance.deactivate_ad()


@receiver(post_save, sender=Ad)
def send_ad_created_email(sender, instance, created, **kwargs):
    if created and instance.user.user.email:
        send_mail(
            subject="Your ad has been created!",
            message=f"Ad '{instance.title}' successfully created!",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.user.user.email],
            fail_silently=False,
        )