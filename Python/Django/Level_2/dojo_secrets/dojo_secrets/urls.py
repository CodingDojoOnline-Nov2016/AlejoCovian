from django.conf.urls import url, include

urlpatterns = [
	url(r'^', include('apps.dojo_users_app.urls', namespace='dojo_users')),
    url(r'^dojo_secrets/', include('apps.dojo_secrets_app.urls', namespace='dojo_secrets')),
]
