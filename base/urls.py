from django.contrib import admin
from django.urls import path, include
from api.models import CourseResource, CategoryResource

course_resource = CourseResource()
category_resource = CategoryResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('api/', include('course_resource.urls')),
    path('api/', include('category_resource.urls')),
]
