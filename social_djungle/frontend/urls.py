from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('frontend.views',
    url(r'^/?$', 'index'),
    url(r'^(\w+)', 'getURL'),
)