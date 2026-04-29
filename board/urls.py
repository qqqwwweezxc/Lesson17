from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('lastmonth/', views.get_ad_last_month, name='last_month'),
    path('activeads/', views.active_ads_in_category, name='active_ads'),
    path('comments/', views.count_comments, name='count_comments'),
    path('useradds/', views.all_user_ads, name='user_adds'),
]