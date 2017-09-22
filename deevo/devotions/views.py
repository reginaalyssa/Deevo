from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView

from formtools.wizard.views import SessionWizardView

from bible.models import *
from bible.views import get_version_model_from_abbr, get_version_model_from_id
from .forms import ChooseVerseForm, ReflectionForm
from .models import Devotion

FORMS = [('choose_verse', ChooseVerseForm),
         ('reflect', ReflectionForm)]

TEMPLATES = {'0': 'devotions/choose.html',
             '1': 'devotions/reflect.html'}

class NewDevotionWizardView(LoginRequiredMixin, SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, form_dict, **kwargs):
        form_dict = {}
        for form in form_list:
            form_dict = dict(form_dict.items() | form.cleaned_data.items())

        new_devotion = Devotion(
            user = self.request.user,
            title = form_dict['title'],
            verse_id = int(str(form_dict['book'].id) + \
                       '{0:03d}'.format(form_dict['chapter']) + \
                       '{0:03d}'.format(form_dict['verse'])),
            version_id = int(form_dict['version'].id),
            reflection = form_dict['reflection'],
            pub_date = timezone.now(),
        )
        new_devotion.save()
        return HttpResponseRedirect(reverse('devotions:view_specific', args=(new_devotion.id,)))

    def get_context_data(self, form, **kwargs):
        context = super(NewDevotionWizardView, self).get_context_data(form=form, **kwargs)
        new_context = self.get_all_cleaned_data()
        if new_context != {}:
            version = new_context['version']
            model = get_version_model_from_abbr(version.abbreviation)
            verse_id = new_context['verse']
            book_id = new_context['book'].id
            chapter_id = new_context['chapter']
            verse = get_object_or_404(model, b=book_id, c=chapter_id, v=verse_id)
            new_context['verse'] = verse
        if self.steps.current == '1':
            context.update(new_context)
        return context

class DevotionListView(LoginRequiredMixin, ListView):
    template_name = 'devotions/view.html'
    context_object_name = 'latest_devotion_list'

    def get_queryset(self):
        """Return the last five published devotions."""
        return Devotion.objects.filter(user_id=self.request.user.id).order_by('-pub_date')[:5]

    def get_context_data(self, **kwargs):
        context = super(DevotionListView, self).get_context_data(**kwargs)
        devotion_list = self.get_queryset()
        verse_list = []
        book_list = []
        version_list = []
        for devotion in devotion_list:
            verse_id = int(devotion.verse_id)
            version_id = int(devotion.version_id)
            model = get_version_model_from_id(version_id)
            verse = get_object_or_404(model, pk=verse_id)
            book = get_object_or_404(KeyEnglish, pk=int(verse.b))
            version = get_object_or_404(BibleVersionKey, id=version_id)
            verse_list.append(verse)
            book_list.append(book)
            version_list.append(version)
        context['zipped_data'] = zip(self.get_queryset(), verse_list, book_list, version_list)
        return context

class UpdateDevotionView(LoginRequiredMixin, UpdateView):
    model = Devotion
    fields = ['title', 'reflection']
    template_name = 'devotions/edit.html'

    def get_success_url(self):
        return reverse('devotions:view_specific', args=(self.get_object().id,))

    def get_context_data(self, **kwargs):
        context = super(UpdateDevotionView, self).get_context_data(**kwargs)
        version_id = self.get_object().version_id
        model = get_version_model_from_id(version_id)
        verse = get_object_or_404(model, pk=self.get_object().verse_id)
        book = get_object_or_404(KeyEnglish, pk=int(verse.b))
        version = get_object_or_404(BibleVersionKey, id=version_id)
        context['verse'] = verse
        context['book'] = book
        context['version'] = version
        return context


class DevotionDetailView(LoginRequiredMixin, DetailView):
    model = Devotion
    template_name = 'devotions/devotion.html'

    def get_context_data(self, **kwargs):
        context = super(DevotionDetailView, self).get_context_data(**kwargs)
        version_id = self.get_object().version_id
        model = get_version_model_from_id(version_id)
        verse = get_object_or_404(model, pk=self.get_object().verse_id)
        book = get_object_or_404(KeyEnglish, pk=int(verse.b))
        version = get_object_or_404(BibleVersionKey, id=version_id)
        context['verse'] = verse
        context['book'] = book
        context['version'] = version
        context['user_id'] = self.get_object().user_id
        return context

def reflect(request, version_id, book_id, chapter_id, verse_id):
    if request.method == 'POST':
        form = ReflectionForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            reflection = form.cleaned_data['reflection']
            version = get_object_or_404(BibleVersionKey, abbreviation=version_id.upper())
            devotion = Devotion(
                user=request.user,
                title=title,
                verse_id=int(str(book_id) + \
                             '{0:03d}'.format(int(chapter_id)) + \
                             '{0:03d}'.format(int(verse_id))),
                version_id=int(version.id),
                reflection=reflection,
                pub_date=timezone.now()
            )
            devotion.save()
            return HttpResponseRedirect(reverse('devotions:view_specific', args=(devotion.pk,)))
    else:
        form = ReflectionForm()

    model = get_version_model_from_abbr(version_id)
    version = get_object_or_404(BibleVersionKey, abbreviation=version_id.upper())
    verse = get_object_or_404(model, b=book_id, c=chapter_id, v=verse_id)
    book = get_object_or_404(KeyEnglish, pk=book_id)
    context = {
        'version': version,
        'verse': verse,
        'book': book,
        'chapter': chapter_id,
        'form': form,
    }
    return render(request, 'devotions/reflect_from_verse.html', context)