from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^key_required$', 'app.views.view_key_required', name='key'),
    url(r'^no_key_required$', 'app.views.view_key_not_required', name='no-key'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)