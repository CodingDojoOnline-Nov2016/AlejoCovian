from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.login_register.urls', namespace='loginregister')),
]
