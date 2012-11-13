# Edit the <mysite>/settings.py file
# go to the INSTALLED_APPS section and uncomment the "django.contrib.admin" app
# it should look similar to this now
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
@h@    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'polls',
)

# Run python manage.py syncdb. Since you have added a new application to INSTALLED_APPS, the database tables need to be updated.


# Edit your <mysite>/urls.py file and uncomment the lines that reference the admin – there are three lines in
# total to uncomment. This file is a URLconf; we’ll dig into URLconfs in the next tutorial. For now, all you need
# to know is that it maps URL roots to applications. In the end, you should have a urls.py file that looks like this:

@h@from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
@h@from django.contrib import admin
@h@admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
@h@    url(r'^admin/', include(admin.site.urls)),
)

# view the Admin Side here: http://127.0.0.1:8000/admin/
