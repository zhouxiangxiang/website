from django.conf.urls import include, url
from django.contrib import admin

import blog

urlpatterns = [
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    url(r'^$',     include('blog.urls')),
    url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^blog/', include(blog.urls)),
]
