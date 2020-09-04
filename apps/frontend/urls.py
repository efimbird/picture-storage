from django.urls import path
from apps.frontend.views import PicturesView, SearchView

urlpatterns = [
    path('', PicturesView.as_view()),
    path('search/', SearchView.as_view()),
]
