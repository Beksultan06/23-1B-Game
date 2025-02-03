from django.urls import path
from app.news.views import NewsView, NewsDetailView

urlpatterns = [
    path("news/", NewsView.as_view(), name='news'),
    path("news/<int:pk>/", NewsDetailView.as_view(), name='news_detail')
]