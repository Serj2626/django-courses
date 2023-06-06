from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from shop.models import Category, Course
from .authentication import CustomAuthentication

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_method = ['get']


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_method = ['get', 'post', 'delete']
        authentication = CustomAuthentication()
        authorization = Authorization()