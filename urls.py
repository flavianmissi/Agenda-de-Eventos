from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'agenda.views.lista'),
    (r'^adiciona/?$', 'agenda.views.adiciona'),
    (r'^item/(?P<item_id>\d+)/?$', 'agenda.views.item'),
    (r'^remove/(?P<item_id>\d+)/?$', 'agenda.views.remove'),
    # Example:
    # (r'^gerenciador/', include('gerenciador.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns+= patterns('',
        url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_DOC_ROOT}),
    )
