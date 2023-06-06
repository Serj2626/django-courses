from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api.models import CourseResource, CategoryResource
from tastypie.api import Api

api = Api(api_name='v1')
course_resource = CourseResource()
category_resource = CategoryResource()
api.register(course_resource)
api.register(category_resource)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('api/', include(api.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
