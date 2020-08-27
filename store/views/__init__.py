from django.shortcuts import render
from django.views.generic import TemplateView
from store.models import Picture
from store.models.forms import PictureForm


class ListPicturesView(TemplateView):
    template_name = 'list_pictures.html'

    def get(self, request, *args, **kwargs):
        pictures = Picture.objects.all()
        return render(request, self.template_name, {'pictures': pictures})


class AddPictureView(TemplateView):
    template_name = 'add_picture.html'

    def get(self, request, *args, **kwargs):
        form = PictureForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            next_form = PictureForm()
            return render(request, self.template_name, {
                'form': next_form,
                'status': 'successful'
            })

        return render(request, self.template_name, {
            'form': form,
            'status': 'failed',
            'errors': form.errors
        })
