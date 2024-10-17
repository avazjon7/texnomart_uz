from django.db.models.signals import pre_delete, post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Category, Product
import json
import os
from django.conf import settings



@receiver(post_save, sender=Category)
@receiver(post_save, sender=Product)
def send_creation_email(sender, instance, created, **kwargs):
    if created:
        subject = f"{instance.__class__.__name__} Created Successfully"
        message = f"{instance.__class__.__name__} '{instance}' has been created successfully."
        recipient_list = ['jasurmavlonov02@gmail.com']
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            recipient_list,
            fail_silently=False,
        )


@receiver(pre_delete, sender=Category)
@receiver(pre_delete, sender=Product)
def save_to_json_before_delete(sender, instance, **kwargs):
    file_path = os.path.join(settings.BASE_DIR, 'deleted_data.json')


    data = {
        "model": instance.__class__.__name__,
        "data": {
            "id": instance.id,
            "name": getattr(instance, 'name', None),
            "title": getattr(instance, 'title', None),
            "created_at": instance.created_at.strftime('%Y-%m-%d %H:%M:%S') if instance.created_at else None,
            "updated_at": instance.updated_at.strftime('%Y-%m-%d %H:%M:%S') if instance.updated_at else None,
        }
    }


    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
    else:
        existing_data = []


    existing_data.append(data)


    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)
