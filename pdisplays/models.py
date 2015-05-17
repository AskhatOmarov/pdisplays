from django.db import models
from geoposition.fields import GeopositionField
from pdisplays import utils

class Display(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    position = GeopositionField(default='0.0, 0.0')
    date_created = models.DateTimeField(blank=True, auto_now_add=True)
    date_edited = models.DateTimeField(blank=True, auto_now=True)

    def __unicode__(self):
        return self.title

    def add_description(self, json):
        description = Description(display=self)
        description.save()
        for v in json:
            try:
                section_field = SectionField.objects.get(slug=v['slug'])
                value = Value(section_field=section_field,
                              description=description, 
                              value=v['value'])
                value.save()
            except SectionField.DoesNotExist:
                return False
        return True

class Description(models.Model):
    display = models.ForeignKey(Display, related_name='descriptions', null=True, blank=True)
    date_created = models.DateTimeField(blank=True, auto_now_add=True)
    date_edited = models.DateTimeField(blank=True, auto_now=True)

class Section(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(blank=True, auto_now_add=True)
    date_edited = models.DateTimeField(blank=True, auto_now=True)

    def __unicode__(self):
        return self.title

class SectionField(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=100, null=True, blank=True)
    help_text = models.CharField(max_length=500, null=True, blank=True)
    section = models.ForeignKey(Section, related_name='fields', null=True, blank=True)
    date_created = models.DateTimeField(blank=True, auto_now_add=True)
    date_edited = models.DateTimeField(blank=True, auto_now=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = utils.slugify(self.title)
        super(SectionField, self).save(*args, **kwargs)

class Value(models.Model):
    value = models.CharField(max_length=100, null=True, blank=True)
    section_field = models.ForeignKey(SectionField, null=True, blank=True)
    description = models.ForeignKey(Description, related_name='values', null=True, blank=True)
    date_created = models.DateTimeField(blank=True, auto_now_add=True)
    date_edited = models.DateTimeField(blank=True, auto_now=True)
