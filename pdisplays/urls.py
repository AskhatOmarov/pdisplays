from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.core.urlresolvers import reverse_lazy
from django.contrib import admin

from pdisplays.views import (
    DisplayView,
    DisplayDetailView,
    DisplayCreateView,
    DisplayEditView,
    DisplayDescriptionFormView,
    DisplayDescriptionDetailView,
)

from tastypie.api import Api
from pdisplays.api import DisplayResource, FormResource

v1_api = Api(api_name='v1')
v1_api.register(DisplayResource())
v1_api.register(FormResource())

from users.models import User
from pdisplays.models import Display, Description#, Section, SectionField

admin.site.register(User)
admin.site.register(Display)
admin.site.register(Description)
# admin.site.register(Section)

# @admin.register(SectionField)
# class SectionFieldAdmin(admin.ModelAdmin):
#     exclude = ('slug',)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdisplays.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('users.urls')),
    url(r'api/doc/', include('tastypie_swagger.urls', namespace='tastypie_swagger'),
        kwargs={"tastypie_api_module":v1_api, "namespace":"tastypie_swagger"}),
    url(r'^api/', include(v1_api.urls)),
    url(r'^$', DisplayView.as_view(
        template_name = 'pdisplays/home.html'),
        name='home-displays',
    ),
    url(r'^displays/$', DisplayView.as_view(
        template_name = 'pdisplays/displays.html'),
        name='all-displays',
    ),
    url(r'^displays/map$', DisplayView.as_view(
        template_name = 'pdisplays/displays-map.html'),
        name='all-displays-map',
    ),
    url(r'^displays/(?P<pk>\d+)/$', DisplayDetailView.as_view(
        template_name = 'pdisplays/display.html'),
        name='view-display',
    ),
    url(r'^displays/new$', DisplayCreateView.as_view(
        template_name = 'pdisplays/display_form.html',
        success_url = reverse_lazy('all-displays')),
        name='new-display',
    ),
    url(r'^displays/edit/(?P<pk>\d+)/$', DisplayEditView.as_view(
        template_name = 'pdisplays/display_form.html',
        success_url = reverse_lazy('all-displays')),
        name='edit-display',
    ),
    url(r'^displays/(?P<pk>\d+)/descriptions/new$', DisplayDescriptionFormView.as_view(
        template_name = 'pdisplays/description_form.html',
        success_url = reverse_lazy('all-displays')),
        name='new-description',
    ),
    url(r'^displays/(?P<disp_pk>\d+)/descriptions/(?P<pk>\d+)$', DisplayDescriptionDetailView.as_view(
        template_name = 'pdisplays/description.html'),
        name='view-description',
    ),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
