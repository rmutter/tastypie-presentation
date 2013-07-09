
from django.conf.urls import patterns, include, url
from django.contrib import admin

from mezzanine.core.views import direct_to_template
from tastypie.api import Api
from slides.api.resources import BlogPostResource, BlogCategoryResource, VersionResource


admin.autodiscover()

v1_api = Api()
v1_api.register(BlogPostResource())
v1_api.register(BlogCategoryResource())
v1_api.register(VersionResource())

urlpatterns = patterns("",

    # Change the admin prefix here to use an alternate URL for the
    # admin interface, which would be marginally more secure.
    ("^admin/", include(admin.site.urls)),

    url("^$", direct_to_template, {"template": "slides.html"}, name="home"),

    url(r'^api/', include(v1_api.urls)),

    ("^", include("mezzanine.urls")),

)

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
