"""carles_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
#from larb import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    # prevent the extra are-you-sure-you-want-to-logout step on logout
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    url(r'^', include('larb.urls')),
    # url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^larb/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),

)
