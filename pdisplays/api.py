from django.conf.urls import url
from django.http import HttpResponse
from tastypie import fields, http
from tastypie.resources import Resource, ModelResource
from tastypie.utils import trailing_slash

from pdisplays.models import Display, Description, Value


class ValueResource(ModelResource):
    section_field = fields.CharField(attribute='section_field')

    class Meta:
        queryset = Value.objects.all()
        resource_name = 'value'
        include_resource_uri = False
        excludes = ['id', 'date_created', 'date_edited']

    def dehydrate(self, bundle):

        from pdisplays.models import SectionField
        bundle.data['slug'] = SectionField.objects.get(title=bundle.data['section_field']).slug
        bundle.data.pop('section_field')
        return bundle

class DescriptionResource(ModelResource):
    values = fields.ToManyField(ValueResource, 'values', full=True)

    class Meta:
        queryset = Description.objects.all()
        include_resource_uri = False
        resource_name = 'description'

class DisplayResource(ModelResource):
    descriptions = fields.ToManyField(DescriptionResource, 'descriptions', full=True)

    class Meta:
        queryset = Display.objects.all()
        resource_name = 'display'
        detail_allowed_methods = ['get', 'post']

    def prepend_urls(self):
        return [
            url(
                r"^(?P<resource_name>%s)/(?P<id>\d+)/add_description%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('add_description'),
                name='api_add_description'
            ),
        ]

    def add_description(self, request, *args, **kwargs):
        if request.method != 'POST':
            return http.HttpNotFound()
        
        basic_bundle = self.build_bundle(request=request)
        # get sales_cycle
        try:
            obj = self.cached_obj_get(bundle=basic_bundle,
                                      **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return http.HttpNotFound()
        except MultipleObjectsReturned:
            return http.HttpMultipleChoices(
                "More than one resource is found at this URI.")

        deserialized = self.deserialize(
            request, request.body,
            format=request.META.get('CONTENT_TYPE', 'application/json'))
        rv = obj.add_description(deserialized)
        return self.create_response(request, {'success': rv}, response_class=http.HttpAccepted)

class FormResource(Resource):
    class Meta:
        resource_name = 'form'

    def prepend_urls(self):
        return [
            url(
                r"^(?P<resource_name>%s)/get_form%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_form'),
                name='api_get_form'
            ),
        ]

    def get_form(self, request, *args, **kwargs):
        
        from pdisplays.forms import prepare_sections

        form = prepare_sections()

        return self.create_response(
                request, {'form': form}
            )
