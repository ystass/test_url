from django.urls import path

from short_url.apps import ShortUrlConfig
from short_url.views import CreateShortUrl, GetOriginalUrl

app_name = ShortUrlConfig.name

urlpatterns = [
    path("", CreateShortUrl.as_view(), name="create_short_url"),
    path("<str:short_url>/", GetOriginalUrl.as_view(), name="get_original_url"),
]

