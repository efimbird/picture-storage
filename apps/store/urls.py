from django.urls import path
from apps.store.views import AddPictureView, EditPictureView, \
    PictureDetailView, DeletePictureView, PictureListCreate

urlpatterns = [
    path('add/', AddPictureView.as_view()),
    path('edit/<int:picture_id>/', EditPictureView.as_view()),
    path('picture/<int:pk>/', PictureDetailView.as_view()),
    path('delete/', DeletePictureView.as_view()),
    path('api/pictures/', PictureListCreate.as_view()),
    path('api/search/', PictureListCreate.as_view())
]