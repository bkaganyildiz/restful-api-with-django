from django.conf.urls import url
from .views import SnippetDetail, snippet_list
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', snippet_list),
    url(r'^(?P<pk>[0-9]+)/$', SnippetDetail.as_view())
]