from app.settings.models import ContactFrom

def create_comment(name, email, comment):
    return ContactFrom.objects.create(
        name=name,
        email=email,
        comment=comment
    )