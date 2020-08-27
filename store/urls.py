from django.urls import path
from store.views import ListPicturesView, AddPictureView

urlpatterns = [
    path('', ListPicturesView.as_view()),
    path('add/', AddPictureView.as_view()),
    # delete, edit, filter
]