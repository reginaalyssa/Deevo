from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.views import generic

from .models import KeyEnglish, TBbe

class BookView(generic.ListView):
    template_name = 'bible/index.html'
    model = KeyEnglish

class ChapterView(generic.DetailView):
    template_name = 'bible/chapter.html'
    model = TBbe
    context_object_name = 'verse_list'

    def get_queryset(self):
        """
        Get all verses in given chapter.
        """
        return TBbe.objects.filter(b = book_id, c = chapter_id)

def chapter(request, book_id, chapter_id):
    verse_list = get_list_or_404(TBbe, b=book_id, c=chapter_id)
    book = get_object_or_404(KeyEnglish, pk=book_id)
    context = {
        'verse_list': verse_list,
        'book': book,
        'chapter': chapter_id,
    }
    return render(request, 'bible/chapter.html', context)

def verse(request, book_id, chapter_id, verse_id):
    verse = get_object_or_404(TBbe, b=book_id, c=chapter_id, v=verse_id)
    book = get_object_or_404(KeyEnglish, pk=book_id)
    context = {
        'verse': verse,
        'book': book,
        'chapter': chapter_id,
    }
    return render(request, 'bible/verse.html', context)