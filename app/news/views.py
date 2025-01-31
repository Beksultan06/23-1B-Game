from django.shortcuts import render
from app.settings.models import ContactFrom
from django.views.generic import TemplateView
# Create your views here.

class NewsView(TemplateView):
    model = ContactFrom
    template_name = 'news/news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactFrom.objects.filter(is_active=True)
        return context