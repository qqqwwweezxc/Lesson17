from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from . import models


def index(request: HttpRequest) -> HttpResponse:
    """Renders the main page."""
    return HttpResponse("Main page")


def get_ad_last_month(request: HttpRequest) -> HttpResponse:
    """Renders the ads last month page."""
    last_month_ads = models.Ad.objects.filter(
        created_at__gte=timezone.now() - timedelta(days=30)
    )
    return render(request, 'board/last_month.html', {'last_month_ads': last_month_ads})


def active_ads_in_category(request: HttpRequest) -> HttpResponse:
    """Renders the active ads page."""
    category = models.Category.objects.get(id=1)

    active_ads = models.Ad.objects.filter(
        category=category,
        is_active=True
    )

    return render(request, 'board/active_ads.html', {
        'active_ads': active_ads,
        'category': category
    })


def count_comments(request: HttpRequest) -> HttpResponse:
    """Renders the comment count page."""
    ads_with_comments = models.Ad.objects.annotate(
        comment_count=Count('comments'),
    )

    return  render(request, 'board/comments.html', context={'ads_with_comments': ads_with_comments})


def all_user_ads(request: HttpRequest) -> HttpResponse:
    """Renders the all user ads page."""
    user = models.UserProfile.objects.get(id=1)

    user_ads = models.Ad.objects.filter(user=user)

    return render(request, 'board/user_adds.html', context={'user_ads': user_ads, 'user': user})