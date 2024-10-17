from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    title = models.CharField(max_length=200, null=True, blank=True, unique=True)
    image = models.ImageField(upload_to='category/%Y/%m/%d/', null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Product(BaseModel):
    name = models.CharField(max_length=200, null=True, blank=True, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True, default=0)
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    users_like = models.ManyToManyField(User, related_name='products', blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Image(BaseModel):
    image = models.ImageField(upload_to='image/%Y/%m/%d/', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='images')
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f'Image for {self.product.name}'


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='orders')
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)
    first_payment = models.FloatField(null=True, blank=True, default=0)
    month = models.PositiveSmallIntegerField(default=3, null=True, blank=True,
                                             validators=[MinValueValidator(3), MaxValueValidator(12)])
    image = models.ImageField(upload_to='order/%Y/%m/%d/', null=True, blank=True)

    @property
    def monthly_payment(self):
        return self.product.price / self.month

    def __str__(self):
        return f'{self.product.name} - {self.user.username} - {self.quantity}'


class Comment(BaseModel):
    class RatingChoices(models.IntegerChoices):
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    message = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='comments/%Y/%m/%d/', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='comments')
    rating = models.PositiveSmallIntegerField(choices=RatingChoices.choices, default=RatingChoices.ZERO, null=True)
    image = models.ImageField(upload_to='comment/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.product.name}'


class AttributeKey(models.Model):
    key_name = models.CharField(max_length=200, null=True, blank=True, unique=True)
    image = models.ImageField(upload_to='attribute_key/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.key_name


class AttributeValue(BaseModel):
    key_value = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='attribute_value/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return self.key_value


class ProductAttribute(models.Model):
    attr_key = models.ForeignKey(AttributeKey, on_delete=models.CASCADE, null=True, blank=True)
    attr_value = models.ForeignKey(AttributeValue, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name='attributes')
    image = models.ImageField(upload_to='product_attribute/%Y/%m/%d/', null=True, blank=True)

    def __str__(self):
        return f'{self.attr_key.key_name}: {self.attr_value.key_value} ({self.product.name})'
