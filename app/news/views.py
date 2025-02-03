from django.shortcuts import render, redirect
from app.settings.models import ContactFrom
from app.news.models import Comment
from django.views.generic import ListView, DetailView
# Create your views here.

class NewsView(ListView):
    model = ContactFrom
    template_name = 'news/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactFrom.objects.filter(is_active=True)
        return context

class NewsDetailView(DetailView):
    model = Comment
    template_name = "news/news-detail.html"
    context_object_name = 'news_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = Comment.objects.all()
        return context

    def post(self, request, *a, **kg):
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get('comment')

        if name and email and comment:
            Comment.objects.create(
                name=name,
                email=email,
                comment=comment
            )

        return redirect("news")