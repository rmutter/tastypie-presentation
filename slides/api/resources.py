from django.conf import settings
from tastypie.bundle import Bundle
from tastypie.constants import ALL_WITH_RELATIONS
from tastypie.fields import ToManyField, CharField
from tastypie.resources import ModelResource, Resource
from mezzanine.blog.models import BlogPost, BlogCategory

__author__ = 'rudy'


class BlogCategoryResource(ModelResource):
    class Meta:
        queryset = BlogCategory.objects.all()
        resource_name = "blog_category"
        filtering = {
            'title': ['exact', 'contains']
        }


class BlogPostResource(ModelResource):
    categories = ToManyField(BlogCategoryResource, 'categories', full=True)

    class Meta:
        queryset = BlogPost.objects.all()
        resource_name = "blog_post"
        filtering = {
            'categories': ALL_WITH_RELATIONS,
            'title': ['exact', 'contains']
        }


class Version(object):
    def __init__(self, identifier=None):
        self.identifier = identifier


class VersionResource(Resource):
    identifier = CharField(attribute='identifier')

    class Meta:
        resource_name = 'version'
        allowed_methods = ['get']
        object_class = Version
        include_resource_uri = False

    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = {}

        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.identifier
        else:
            kwargs['pk'] = bundle_or_obj['identifier']

        return kwargs

    def get_object_list(self, bundle, **kwargs):
        return [Version(identifier=settings.VERSION)]

    def obj_get_list(self, bundle, **kwargs):
        return self.get_object_list(bundle, **kwargs)