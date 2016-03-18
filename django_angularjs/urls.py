from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from rest_framework.routers import DefaultRouter

from apps.poll.views import ChoiceModelViewSet, PollModelViewSet

router = DefaultRouter()
router.register(r'poll', PollModelViewSet, base_name='polls')
router.register(r'choice', ChoiceModelViewSet, base_name='choices')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += patterns('',
                           url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                               {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                           ) + staticfiles_urlpatterns() + urlpatterns