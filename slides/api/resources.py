from tastypie.fields import ToManyField
from tastypie.resources import ModelResource
from mezzanine.blog.models import BlogPost, BlogCategory

__author__ = 'rudy'


class BlogCategoryResource(ModelResource):
    class Meta:
        queryset = BlogCategory.objects.all()
        resource_name = "blog_category"


class BlogPostResource(ModelResource):
    categories = ToManyField(BlogCategoryResource, 'categories', full=True)

    class Meta:
        queryset = BlogPost.objects.all()
        resource_name = "blog_post"