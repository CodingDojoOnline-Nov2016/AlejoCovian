
from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.product_app.urls', namespace='products')),
]




