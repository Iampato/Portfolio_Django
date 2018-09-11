from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from filebrowser.sites import site
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
 'posts': PostSitemap,
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/filebrowser/',include(site.urls)),
    url('', include('home.urls', namespace='home', app_name='home')),
    url('blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
            name='django.contrib.sitemaps.views.sitemap'),
    url(r'^tinymce/', include('tinymce.urls')),
]


if settings.DEBUG:
    urlpatterns += static (settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
else:
	urlpatterns += static (settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 


