from django.views import generic

from .models import KeyEnglish

class BookView(generic.ListView):
    template_name = 'bible/index.html'
    model = KeyEnglish