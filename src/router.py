from django.urls import include, path

urlpatterns = [
    path("docs/", include("src.docs.urls")),
    path("", include("src.api.urls")),
]
