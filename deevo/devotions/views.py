from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils import timezone

from formtools.wizard.views import SessionWizardView

from bible.models import *
from .forms import ChooseVerseForm, ReflectionForm
from .models import Devotion

FORMS = [('choose_verse', ChooseVerseForm),
         ('reflect', ReflectionForm)]

TEMPLATES = {'0': 'devotions/choose.html',
             '1': 'devotions/reflect.html'}

class NewDevotionWizard(SessionWizardView):
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
        return HttpResponseRedirect('/')

    def get_context_data(self, form, **kwargs):
        context = super(NewDevotionWizard, self).get_context_data(form=form, **kwargs)
        new_context = self.get_all_cleaned_data()
        if new_context != {}:
            version = new_context['version']
            if version.abbreviation == 'ASV':
                model = TAsv
            elif version.abbreviation == 'BBE':
                model = TBbe
            elif version.abbreviation == 'DARBY':
                model = TDby
            elif version.abbreviation == 'KJV':
                model = TKjv
            elif version.abbreviation == 'WBT':
                model = TWbt
            elif version.abbreviation == 'WEB':
                model = TWeb
            elif version.abbreviation == 'YLT':
                model = TYlt
            else:
                raise Http404("Bible version does not exist")
            verse_id = new_context['verse']
            book_id = new_context['book'].id
            chapter_id = new_context['chapter']
            verse = get_object_or_404(model, b=book_id, c=chapter_id, v=verse_id)
            new_context['verse'] = verse
        if self.steps.current == '1':
            context.update(new_context)
        return context