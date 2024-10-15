from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Product, Order
from django.utils.text import slugify


@receiver(pre_save, sender=Product)
def add_slug_to_product(sender, instance, **kwargs):

    if not instance.slug:
        instance.slug = slugify(instance.name)


@receiver(post_save, sender=Order)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        if product.quantity >= instance.quantity:
            product.quantity -= instance.quantity
            product.save()
        else:
            raise ValueError(f"Mahsulotda yetarli zaxira mavjud emas: {product.name}")
