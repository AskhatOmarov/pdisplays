from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView

from pdisplays.models import Display, Description, Value, Section, SectionField
from pdisplays.forms import DescriptionForm
from pdisplays import utils

class DisplayView(ListView):
    model = Display

    def get_context_data(self, *args, **kwargs):
        context = super(DisplayView, self).get_context_data(*args, **kwargs)
        s = self.request.GET.get('s', None)
        context['search'] = s
        return context

    def get_queryset(self):
        s = self.request.GET.get('s', None)
        if s != None:
            return Display.objects.filter(title__icontains=s)
        return super(DisplayView, self).get_queryset()

class DisplayDetailView(DetailView):
    model = Display
    
class DisplayCreateView(CreateView):
    model = Display
    
class DisplayEditView(UpdateView):
    model = Display

class DisplayDescriptionFormView(FormView):
    form_class = DescriptionForm

    def post(self, request, *args, **kwargs):
    	post_data = request.POST.copy()
    	del post_data['csrfmiddlewaretoken']
    	display_id = kwargs.get('pk')
    	description = Description(display_id=display_id)
    	description.save()
    	for k in post_data:
    		try:
    			sf = SectionField.objects.get(slug=utils.slugify(k))
    			v = Value(value=post_data[k],
    					  section_field=sf,
    					  description=description)
    			v.save()
    		except SectionField.DoesNotExist:
    			pass
    	return super(DisplayDescriptionFormView, self).post(request, *args, **kwargs)

class DisplayDescriptionDetailView(DetailView):
    model = Description

    def get_context_data(self, *args, **kwargs):
        context = super(DisplayDescriptionDetailView, self).get_context_data(*args, **kwargs)
        context['sections'] = Section.objects.all()
        context['section_fields'] = SectionField.objects.all()
        return context

class StatisticsView(TemplateView):
    model = Description

    def get_context_data(self, *args, **kwargs):
        context = super(DisplayDescriptionDetailView, self).get_context_data(*args, **kwargs)
        context['sections'] = Section.objects.all()
        context['section_fields'] = SectionField.objects.all()
        return context
