from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('apps.loginregister.urls', namespace='loginregister')),
    url(r'^courses/', include('apps.courses_app_2ndtry.urls', namespace='courses')),
    url(r'^surveyform/', include('apps.surveyform.urls', namespace='surveyform')),
    url(r'^randomwords/', include('apps.random_words.urls', namespace='randomwords')),
    url(r'^timedisplay/', include('apps.timedisplay.urls', namespace='timedisplay')),
]
