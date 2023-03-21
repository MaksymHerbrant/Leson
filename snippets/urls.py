from django.urls import path
from snippets.views import snippets_list

urlpatterns = [
    path('snippets', snippets_list)
]
