from django.urls import path
from store.views import ListPicturesView, AddPictureView, EditPictureView, PictureDetailsView

urlpatterns = [
    path('', ListPicturesView.as_view()),
    path('add/', AddPictureView.as_view()),
    path('edit/<int:picture_id>/', EditPictureView.as_view()),
    path('picture/<int:picture_id>/', PictureDetailsView.as_view()),
    # delete, filter
]