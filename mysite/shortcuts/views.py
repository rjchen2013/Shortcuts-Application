from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse

from django.views.generic import ListView, FormView

from .models import Shortcut
from .forms import ShortcutForm


# Create your views here.
class IndexView(ListView):
    model = Shortcut
    template_name = 'shortcuts/index.html'
    context_object_name = 'shortcut_list'

    def get_queryset(self):
        return Shortcut.objects.order_by('shortcut_cmd')


class ShortcutFormView(FormView):
    template_name = 'shortcuts/detail.html'
    form_class = ShortcutForm
    success_url = reverse_lazy('shortcuts:result')

    def post(self, request, *args, **kwargs):

        form = self.get_form(self.get_form_class())
        shortcut_object = ''
        response = ''

        if form.is_valid():
            if form.cleaned_data['first_key'] == 'Ctrl':
                if form.cleaned_data['second_key'] == 'C':
                    shortcut_object = Shortcut.objects.get(shortcut_cmd='copy')
                elif form.cleaned_data['second_key'] == 'V':
                    shortcut_object = Shortcut.objects.get(shortcut_cmd='paste')
                elif form.cleaned_data['second_key'] == 'S':
                    shortcut_object = Shortcut.objects.get(shortcut_cmd='save')
                elif form.cleaned_data['second_key'] == 'A':
                    shortcut_object = Shortcut.objects.get(shortcut_cmd='select all')
            elif form.cleaned_data['first_key'] == 'Shift':
                if form.cleaned_data['second_key'] == 'Delete':
                    shortcut_object = Shortcut.objects.get(shortcut_cmd='delete permanently')
            elif form.cleaned_data['first_key'] == 'Alt':
                if form.cleaned_data['second_key'] == 'Enter':
                    shortcut_object = Shortcut.objects.get(shortcut_cmd='view properties')
            else:
                pass

            if shortcut_object != '':
                response = shortcut_object.shortcut_desc

                return HttpResponse(response)
            else:
                return HttpResponse("No such keyboard shortcut!")
        else:
            return self.form_invalid(form)