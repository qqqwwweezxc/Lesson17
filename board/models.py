from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.core.validators import MinValueValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def active_ads_count(self):
        return self.ads.filter(is_active=True).count()

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ads')

    def show_description(self):
        return self.description[:100]

    def deactivate_ad(self):
        if self.created_at <= timezone.now() - timedelta(days=30):
            self.is_active = False
            self.save(update_fields=['is_active'])

    def count_comments(self):
        return self.comments.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.user} on {self.ad}"


