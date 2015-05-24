from form_utils import forms as better_forms
from django import forms

from pdisplays.models import Description

# def prepare_sections():
#     sections = Section.objects.all()

#     def get_section_fields(section):
#         return SectionField.objects.filter(section_id=section.id)

#     return [(s.title, 
#             {
#                 'fields': [sf.title for sf in get_section_fields(s)], 
#                 'legend': s.title,
#             }) for s in sections 
#             ]

class DescriptionForm(better_forms.BetterForm):

    def __init__(self, *args, **kwargs):
        super(DescriptionForm, self).__init__(*args, **kwargs)
        
        for f in SectionField.objects.all():
            self.fields[f.title] = forms.CharField(
                label=f.title,
                required=False,
            )

    # class Meta:
    #     fieldsets = prepare_sections()

class DescriptionModelForm(better_forms.BetterModelForm):  
    class Meta:  
        model = Description  
        exclude = ('display',)  
        fieldsets = [('Technical parameters', {
                   'fields': ['size', 'power_consumption', 'resolution', 'type', 'input_formats', 'viewing_distance', 'manufacturer', 'model'],
                   'description': 'Information',  
                  }),
                  ('Experience', {
                   'fields': ['vision_quality', 'content_relevance', 'interaction_potential', 'common_impression'],
                   'description': 'Information2',  
                  }),
                  ('Deployment', {
                   'fields': ['crowd_coverage', 'indoor_outdoor', 'mode_of_operation', 'surroundings', 'total_score'],
                   'description': 'Information3',  
                  }),]  
