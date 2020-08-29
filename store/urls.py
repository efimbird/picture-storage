from django.urls import path
from store.views import PicturesListView, AddPictureView, EditPictureView, \
    PictureDetailView, DeletePictureView

urlpatterns = [
    path('', PicturesListView.as_view()),
    path('add/', AddPictureView.as_view()),
    path('edit/<int:picture_id>/', EditPictureView.as_view()),
    path('picture/<int:pk>/', PictureDetailView.as_view()),
    path('delete/', DeletePictureView.as_view()),
    # filter
]