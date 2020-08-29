from django.http import Http404, JsonResponse
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
            Picture.clear_obsolete_trash()
            return JsonResponse({'status': 'successful'})

        return JsonResponse({
            'status': 'failed',
            'errors': form.errors
        })


class PictureDetailsView(TemplateView):
    template_name = 'picture_details.html'

    def get(self, request, picture_id=-1, *args, **kwargs):
        picture = _get_picture(picture_id)
        return render(request, self.template_name, {'picture': picture})


class EditPictureView(TemplateView):
    template_name = 'edit_picture.html'

    def get(self, request, picture_id=-1, *args, **kwargs):
        picture = _get_picture(picture_id)
        form = PictureForm(instance=picture)
        return render(request, self.template_name, {
            'form': form,
            'picture_id': picture_id
        })

    def post(self, request, picture_id=-1, *args, **kwargs):
        picture = _get_picture(picture_id)
        form = PictureForm(request.POST, request.FILES, instance=picture)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'successful'})

        return JsonResponse({
            'status': 'failed',
            'errors': form.errors
        })


class DeletePictureView(TemplateView):
    template_name = 'restore_picture.html'

    def post(self, request, *args, **kwargs):
        if request.POST['action'] == 'delete':
            picture = _get_picture(request.POST['picture_id'])
            picture.delete()
            # return JsonResponse({'status': 'successful'})
            return render(request, self.template_name, {'picture_id': request.POST['picture_id']})
        elif request.POST['action'] == 'undo':
            picture = _get_trashed_picture(request.POST['picture_id'])
            picture.restore()
            return JsonResponse({'status': 'successful'})

        return JsonResponse({
            'status': 'failed',
            'errors': 'Incorrect action'
        })


def _get_picture(picture_id):
    try:
        picture = Picture.objects.get(pk=picture_id)
        return picture
    except Picture.DoesNotExist:
        raise Http404("Picture not Found")


def _get_trashed_picture(picture_id):
    try:
        picture = Picture.trash.get(pk=picture_id)
        return picture
    except Picture.DoesNotExist:
        raise Http404("Picture not Found")
