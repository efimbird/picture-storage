from django.http import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from store.models import Picture
from store.models.forms import PictureForm


class PicturesListView(ListView):
    template_name = 'list_pictures.html'
    model = Picture
    paginate_by = 2
    context_object_name = 'pictures'


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


class PictureDetailView(DetailView):
    template_name = 'picture_details.html'
    model = Picture
    context_object_name = 'picture'


class EditPictureView(TemplateView):
    template_name = 'edit_picture.html'

    def get(self, request, picture_id=-1, *args, **kwargs):
        picture = get_object_or_404(Picture, pk=picture_id)
        form = PictureForm(instance=picture)
        return render(request, self.template_name, {
            'form': form,
            'picture_id': picture_id
        })

    def post(self, request, picture_id=-1, *args, **kwargs):
        picture = get_object_or_404(Picture, pk=picture_id)
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
            picture = get_object_or_404(Picture, pk=request.POST['picture_id'])
            picture.delete()
            # return JsonResponse({'status': 'successful'})
            return render(request, self.template_name, {'picture_id': request.POST['picture_id']})
        elif request.POST['action'] == 'undo':
            picture = get_trashed_picture_or_404(request.POST['picture_id'])
            picture.restore()
            return JsonResponse({'status': 'successful'})

        return JsonResponse({
            'status': 'failed',
            'errors': 'Incorrect action'
        })


def get_trashed_picture_or_404(picture_id):
    try:
        picture = Picture.trash.get(pk=picture_id)
        return picture
    except Picture.DoesNotExist:
        raise Http404("Picture not Found")
