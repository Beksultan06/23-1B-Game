from django.urls import path
from app.news.views import NewsView

urlpatterns = [
    path("news/", NewsView.as_view(), name='news')
]