from django.conf.urls import patterns, include, url
# from DjangoApplication.view import earthquake #uncomment the line to support earthquake view

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoApplication.views.home', name='home'),
    # url(r'^DjangoApplication/', include('DjangoApplication.DjangoApplication.urls')),

    # url('^earthquake/$',earthquake), #uncomment the line to support earthquake view

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
