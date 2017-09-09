from django.http import Http404
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.views import generic

from .models import *

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

def chapter(request, version_id, book_id, chapter_id):
    if version_id == 'asv':
        model = TAsv
    elif version_id == 'bbe':
        model = TBbe
    elif version_id == 'darby':
        model = TDby
    elif version_id == 'kjv':
        model = TKjv
    elif version_id == 'wbt':
        model = TWbt
    else:
        raise Http404("Bible version does not exist")
    version = get_object_or_404(BibleVersionKey, abbreviation=version_id.upper())
    verse_list = get_list_or_404(model, b=book_id, c=chapter_id)
    book = get_object_or_404(KeyEnglish, pk=book_id)
    context = {
        'version': version,
        'version_link': version_id,
        'verse_list': verse_list,
        'book': book,
        'chapter': chapter_id,
    }
    return render(request, 'bible/chapter.html', context)

def verse(request, version_id, book_id, chapter_id, verse_id):
    if version_id == 'asv':
        model = TAsv
    elif version_id == 'bbe':
        model = TBbe
    elif version_id == 'darby':
        model = TDby
    elif version_id == 'kjv':
        model = TKjv
    elif version_id == 'wbt':
        model = TWbt
    else:
        raise Http404("Bible version does not exist")
    version = get_object_or_404(BibleVersionKey, abbreviation=version_id.upper())
    verse = get_object_or_404(model, b=book_id, c=chapter_id, v=verse_id)
    book = get_object_or_404(KeyEnglish, pk=book_id)
    context = {
        'version': version,
        'verse': verse,
        'book': book,
        'chapter': chapter_id,
    }
    return render(request, 'bible/verse.html', context)