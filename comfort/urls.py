from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib import admin
from comfortapp.views import TaskViewSet


from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'task', TaskViewSet, 'task')


urlpatterns = [
    # Examples:
    url(r'^task', include(router.urls)),
    url(r'^$', 'comfortapp.views.home', name='home'),
    url(r'^strategies', 'comfortapp.views.strategies', name='strategies'),
    url(r'^test', 'comfortapp.views.myview', name='myview'),
    url(r'^st1', 'comfortapp.views.st1', name='st1'),
    url(r'^st2', 'comfortapp.views.st2', name='st2'),
    url(r'^st3', 'comfortapp.views.st3', name='st3'),
    url(r'^st4', 'comfortapp.views.st4', name='st4'),
    url(r'^viewdata', 'comfortapp.views.viewdata', name='viewdata'),
    url(r'^viewenvmeasurements', 'comfortapp.views.viewenvmeasurements', name='viewenvmeasurements'),






    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
]
