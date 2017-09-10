from django.shortcuts import render, get_list_or_404, get_object_or_404
from bible.models import *

def reflect(request, version_id, book_id, chapter_id, verse_id):
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
        'version_link': version_id,
        'verse': verse,
        'book': book,
        'chapter': chapter_id,
    }
    return render(request, 'devotions/reflect.html', context)