from django.shortcuts import render
from .models import About
from django.contrib import messages
from .forms import RequestForm

# Create your views here.

def about_page(request):
    """
    Renders the About page
    """

    if request.method == 'POST':
        request_form = RequestForm(request.POST)
        if request_form.is_valid():
                request_form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    "You have successfully submitted your request!"
                )


    about = About.objects.all().order_by('date_updated').first()
    request_form = RequestForm()

    return render(
        request,
        "about/about.html",
        {'about': about,
         'request_form': request_form
        },
    )