from django.shortcuts import render
from django.views.generic import TemplateView
from apps.store.models import Picture


class PicturesView(TemplateView):
    template_name = 'pictures.html'
    started_template_name = 'getting-started.html'

    def get_template_names(self):
        if Picture.objects:
            return [self.template_name]
        else:
            return [self.started_template_name]


class SearchView(TemplateView):
    template_name = 'search_pictures.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'searched_text': request.GET['title']})
