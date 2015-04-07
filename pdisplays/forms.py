from form_utils import forms as better_forms
from django import forms

from pdisplays.models import Description, Section, SectionField

def prepare_sections():
    sections = Section.objects.all()

    def get_section_fields(section):
        return SectionField.objects.filter(section_id=section.id)

    return [(s.title, 
            {
                'fields': [sf.title for sf in get_section_fields(s)], 
                'legend': s.title,
            }) for s in sections 
            ]

class DescriptionForm(better_forms.BetterForm):

    def __init__(self, *args, **kwargs):
        super(DescriptionForm, self).__init__(*args, **kwargs)
        
        for f in SectionField.objects.all():
            self.fields[f.title] = forms.CharField(
                label=f.title,
                required=False,
            )

    class Meta:
        fieldsets = prepare_sections()
