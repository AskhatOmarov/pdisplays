from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render_to_response
from tastypie import fields, http
from tastypie.resources import Resource, ModelResource
from tastypie.utils import trailing_slash
from tastypie.authorization import Authorization

from pdisplays.models import Display, Description#, Value, Section, SectionField


# class ValueResource(ModelResource):
#     section_field = fields.CharField(attribute='section_field')

#     class Meta:
#         queryset = Value.objects.all()
#         resource_name = 'value'
#         include_resource_uri = False
#         excludes = ['id', 'date_created', 'date_edited']

#     def dehydrate(self, bundle):

#         from pdisplays.models import SectionField
#         bundle.data['slug'] = SectionField.objects.get(title=bundle.data['section_field']).slug
#         bundle.data.pop('section_field')
#         return bundle

class DescriptionResource(ModelResource):
    # values = fields.ToManyField(ValueResource, 'values', full=True)

    class Meta:
        queryset = Description.objects.all()
        include_resource_uri = False
        resource_name = 'description'

class DisplayResource(ModelResource):
    descriptions = fields.ToManyField(DescriptionResource, 'descriptions', full=True, null=True)

    class Meta:
        queryset = Display.objects.all()
        resource_name = 'display'
        authorization=Authorization()

    def prepend_urls(self):
        return [
            url(
                r"^(?P<resource_name>%s)/(?P<id>\d+)/add_description%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('add_description'),
                name='api_add_description'
            ),
            url(
                r"^(?P<resource_name>%s)/(?P<id>\d+)/get_info%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_info'),
                name='api_get_info'
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

    def get_info(self, request, *args, **kwargs):
        if request.method != 'GET':
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

        return render_to_response('pdisplays/_display_description.html', {
            # Other things here.
            "display": obj,
        })

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
