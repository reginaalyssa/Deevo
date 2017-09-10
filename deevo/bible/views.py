from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.views import generic

from .models import *
from .forms import VersionForm

# class BookView(generic.ListView):
#     template_name = 'bible/index.html'
#     model = KeyEnglish
#
#     def get_initial(self):
#         return {'value1': self.kwargs['version_id']}
#
#     def get_context_data(self, **kwargs):
#         context = super(BookView, self).get_context_data(**kwargs)
#         context['version'] = self.kwargs['version_id']
#         form = VersionForm(self.request.POST or None, initial={"version": self.kwargs['version_id']})
#         context['form'] = form
#         return context

def change_version_book(request):
    if request.method == 'POST':
        form = VersionForm(request.POST)

        if form.is_valid():
            version = form.cleaned_data['version']
            return HttpResponseRedirect(reverse('bible:book', args=(version.abbreviation.lower(),)))

def change_version_chapter(request, book_id, chapter_id):
    if request.method == 'POST':
        form = VersionForm(request.POST)

        if form.is_valid():
            version = form.cleaned_data['version']
            return HttpResponseRedirect(reverse('bible:chapter', args=(version.abbreviation.lower(), book_id, chapter_id,)))

def change_version_verse(request, book_id, chapter_id, verse_id):
    if request.method == 'POST':
        form = VersionForm(request.POST)

        if form.is_valid():
            version = form.cleaned_data['version']
            return HttpResponseRedirect(reverse('bible:verse', args=(version.abbreviation.lower(), book_id, chapter_id, verse_id,)))

def book(request, version_id):
    book_list = get_list_or_404(KeyEnglish)
    version = get_object_or_404(BibleVersionKey, abbreviation=version_id.upper())
    form = VersionForm(request.POST or None, initial={"version": version.id})
    context = {
        'version': version_id,
        'book_list': book_list,
        'form': form,
    }
    return render(request, 'bible/index.html', context)

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
    elif version_id == 'web':
        model = TWeb
    elif version_id == 'ylt':
        model = TYlt
    else:
        raise Http404("Bible version does not exist")
    version = get_object_or_404(BibleVersionKey, abbreviation=version_id.upper())
    verse_list = get_list_or_404(model, b=book_id, c=chapter_id)
    book = get_object_or_404(KeyEnglish, pk=book_id)
    form = VersionForm(request.POST or None, initial={"version": version.id})
    context = {
        'version': version,
        'version_link': version_id,
        'verse_list': verse_list,
        'book': book,
        'chapter': chapter_id,
        'form': form,
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
    form = VersionForm(request.POST or None, initial={"version": version.id})
    context = {
        'version': version,
        'version_link': version_id,
        'verse': verse,
        'book': book,
        'chapter': chapter_id,
        'form': form,
    }
    return render(request, 'bible/verse.html', context)