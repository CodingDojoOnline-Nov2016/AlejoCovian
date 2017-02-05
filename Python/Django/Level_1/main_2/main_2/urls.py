from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.second_app.urls')),
]
