from django.urls import path
from snippets.views import snippets_list, styles_list, language_list

urlpatterns = [
    path('snippets', snippets_list),
    path('styles', styles_list),
    path('languages', language_list)
]
