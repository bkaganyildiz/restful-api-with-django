from django.conf.urls import url
from .views import snippet_detail, snippet_list
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', snippet_list),
    url(r'^(?P<snippet_id>[0-9]+)/$', snippet_detail)
]