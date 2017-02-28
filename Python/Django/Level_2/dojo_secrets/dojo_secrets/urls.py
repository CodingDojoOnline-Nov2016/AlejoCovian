from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.dojo_secrets_app.urls')),
]
