from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView

from .models import *
from .forms import ChapterForm, VerseForm, VersionForm

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

def change_chapter(request, version_id, book_id):
    if request.method == 'POST':
        form = ChapterForm(request.POST, model=get_version_model_from_abbr(version_id), book_id=book_id)

        if form.is_valid():
            chapter = form.cleaned_data['chapter']
        else:
            chapter = form.data['chapter']

        return HttpResponseRedirect(reverse('bible:chapter', args=(version_id, book_id, chapter,)))

def change_verse(request, version_id, book_id, chapter_id):
    if request.method == 'POST':
        form = VerseForm(request.POST, model=get_version_model_from_abbr(version_id), book_id=book_id, chapter_id=chapter_id)

        if form.is_valid():
            verse = form.cleaned_data['verse']
        else:
            verse = form.data['verse']

        return HttpResponseRedirect(reverse('bible:verse', args=(version_id, book_id, chapter_id, verse,)))


def get_version_model_from_abbr(version_abbr):
    version_abbr = version_abbr.lower()
    if version_abbr == 'asv':
        model = TAsv
    elif version_abbr == 'bbe':
        model = TBbe
    elif version_abbr == 'darby':
        model = TDby
    elif version_abbr == 'kjv':
        model = TKjv
    elif version_abbr == 'wbt':
        model = TWbt
    elif version_abbr == 'web':
        model = TWeb
    elif version_abbr == 'ylt':
        model = TYlt
    else:
        raise Http404("Bible version does not exist")
    return model

def get_version_model_from_id(version_id):
    if version_id == 1:
        model = TAsv
    elif version_id == 2:
        model = TBbe
    elif version_id == 3:
        model = TDby
    elif version_id == 4:
        model = TKjv
    elif version_id == 5:
        model = TWbt
    elif version_id == 6:
        model = TWeb
    elif version_id == 7:
        model = TYlt
    else:
        raise Http404("Bible version does not exist")
    return model

class BookListView(LoginRequiredMixin, ListView):
    template_name = 'bible/index.html'
    model = KeyEnglish
    context_object_name = 'book_list'

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        version_id = self.kwargs.get('version_id')
        if not version_id:
            version_id = 'asv'
        version = get_object_or_404(BibleVersionKey, abbreviation=version_id.upper())
        context['form'] = VersionForm(self.request.POST or None, initial={'version': version.id})
        context['version'] = version_id
        return context

class ChapterListView(LoginRequiredMixin, ListView):
    template_name = 'bible/chapter.html'
    context_object_name = 'verse_list'

    def get_queryset(self):
        version_id = self.kwargs.get('version_id')
        model = get_version_model_from_abbr(version_id)
        queryset = get_list_or_404(model, b=self.kwargs.get('book_id'), c=self.kwargs.get('chapter_id'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ChapterListView, self).get_context_data(**kwargs)
        version = get_object_or_404(BibleVersionKey, abbreviation=self.kwargs['version_id'].upper())
        context['version_form'] = VersionForm(self.request.POST or None, initial={'version': version.id})
        context['version'] = version
        context['book'] = get_object_or_404(KeyEnglish, pk=self.kwargs['book_id'])
        context['chapter'] = self.kwargs['chapter_id']
        context['version_link'] = self.kwargs['version_id']
        model = get_version_model_from_id(version.id)
        context['chapter_form'] = ChapterForm(self.request.POST or None, initial={'chapter': context['chapter']}, model=model, book_id=self.kwargs['book_id'])
        return context

class VerseDetailView(LoginRequiredMixin, DetailView):
    template_name = 'bible/verse.html'
    context_object_name = 'verse'

    def get_object(self):
        version_id = self.kwargs.get('version_id')
        model = get_version_model_from_abbr(version_id)
        object = get_object_or_404(model, b=self.kwargs.get('book_id'), c=self.kwargs.get('chapter_id'), v=self.kwargs.get('verse_id'))
        return object

    def get_context_data(self, **kwargs):
        context = super(VerseDetailView, self).get_context_data(**kwargs)
        version = get_object_or_404(BibleVersionKey, abbreviation=self.kwargs['version_id'].upper())
        context['version_form'] = VersionForm(self.request.POST or None, initial={'version': version.id})
        context['version'] = version
        context['book'] = get_object_or_404(KeyEnglish, pk=self.kwargs['book_id'])
        context['chapter'] = self.kwargs['chapter_id']
        context['version_link'] = self.kwargs['version_id']
        model = get_version_model_from_abbr(self.kwargs['version_id'])
        context['verse_form'] = VerseForm(self.request.POST or None, initial={'verse': self.kwargs['verse_id']},
                                              model=model, book_id=self.kwargs['book_id'], chapter_id=self.kwargs['chapter_id'])
        return context