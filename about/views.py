from django.shortcuts import render
from .models import About

# Create your views here.

def about_page(request):
    """
    Renders the About page
    """

    about = About.objects.all().order_by('date_updated').first()

    return render(
        request,
        "about/about.html",
        {'about': about},
    )