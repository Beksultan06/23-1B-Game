from django.shortcuts import render, redirect
from app.settings.models import Banner, Settings, Contact, ContactFrom
from django.views.generic import TemplateView
from app.settings.utils import create_comment

# Create your views here.
# def index(request):
#     banner_all = Banner.objects.all()
#     setting_id = Settings.objects.latest("id")
#     return render(request, "base/index.html", locals())

class IndexView(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner_all'] = Banner.objects.all()
        context['setting_id'] = Settings.objects.latest("id")
        return context

# def contact(request):
    # return render(request, "base/contact.html",locals())

class ContactView(TemplateView):
    template_name = 'base/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_all'] = Contact.objects.all()
        return context

    def post(self, request, *a, **kg):
        name = request.POST.get("name")
        email = request.POST.get("email")
        comment = request.POST.get('comment')

        if name and email and comment:
            create_comment(name, email, comment)

        return redirect("index")