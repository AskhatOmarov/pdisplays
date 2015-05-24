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
    date_created = models.DateTimeField(max_length=100, blank=True, auto_now_add=True)
    date_edited = models.DateTimeField(max_length=100, blank=True, auto_now=True)
    size = models.CharField(max_length=100, blank=True, null=True,
                            choices = (
                                ('small', 'Small: <50cm'),
                                ('medium', 'Medium: <1m'),
                                ('large', 'Large: <3m'),
                                ('extra-large', 'Extra-large: >3m'),
                            ),
                            help_text='Evaluate size of the display')
    power_consumption = models.CharField(max_length=100, blank=True, null=True)
    resolution = models.CharField(max_length=100, blank=True, null=True,
                                  choices = (
                                    ('480p', '480p (720 x 480)'),
                                    ('720p', '720p (1,280 x 720)'),
                                    ('1080p', '1080p (1,920 x 1,080)'),
                                    ('4K UHD', '4K UHD (3,840 x 2,160)'),
                                    ('8K UHD', '8K UHD (7,680 x 4,320)'),
                                  ))
    # aspect_ratio = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True,
                            choices = (
                                ('LED', 'LED'),
                                ('LCD', 'LCD'),
                                ('PDP', 'PDP'),
                            ))
    input_formats = models.CharField(max_length=100, blank=True, null=True,
                            choices = (
                                ('PAL', 'PAL'),
                                ('SECAM', 'SECAM'),
                                ('NTSC', 'NTSC'),
                                ('DVI', 'DVI'),
                                ('VGA', 'VGA'),
                            ))
    viewing_distance = models.CharField(max_length=100, blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True,
                                    choices = (
                                        ('LG', 'LG'),
                                        ('Panasonic', 'Panasonic'),
                                        ('Samsung', 'Samsung'),
                                        ('Sony', 'Sony'),
                                        ('Philips', 'Philips'),
                                    ))
    model = models.CharField(max_length=100, blank=True, null=True)

    vision_quality = models.TextField(blank=True, null=True)
    content_relevance = models.TextField(blank=True, null=True)
    interaction_potential = models.TextField(blank=True, null=True)
    common_impression = models.TextField(blank=True, null=True)

    crowd_coverage = models.CharField(max_length=100, blank=True, null=True)
    indoor_outdoor = models.CharField(max_length=100, blank=True, null=True,
                                      choices = (
                                        ('Indoor', 'Indoor'),
                                        ('Outdoor', 'Outdoor'),
                                      ))
    mode_of_operation = models.CharField(max_length=100, blank=True, null=True,
                                         choices = (
                                            ('part-time', 'Part-time'),
                                            ('24/7', '24/7'),
                                         ))
    surroundings = models.TextField(blank=True, null=True)
    total_score = models.IntegerField(max_length=100, blank=True, null=True,
                                   choices = (
                                            (1, 1),
                                            (2, 2),
                                            (3, 3),
                                            (4, 4),
                                            (5, 5),
                                         ))


# class Section(models.Model):
#     title = models.CharField(max_length=100, null=True, blank=True)
#     date_created = models.DateTimeField(blank=True, auto_now_add=True)
#     date_edited = models.DateTimeField(blank=True, auto_now=True)

#     def __unicode__(self):
#         return self.title

# class SectionField(models.Model):
#     title = models.CharField(max_length=100, null=True, blank=True)
#     slug = models.CharField(max_length=100, null=True, blank=True)
#     help_text = models.CharField(max_length=500, null=True, blank=True)
#     section = models.ForeignKey(Section, related_name='fields', null=True, blank=True)
#     date_created = models.DateTimeField(blank=True, auto_now_add=True)
#     date_edited = models.DateTimeField(blank=True, auto_now=True)

#     def __unicode__(self):
#         return self.title

#     def save(self, *args, **kwargs):
#         self.slug = utils.slugify(self.title)
#         super(SectionField, self).save(*args, **kwargs)

# class Value(models.Model):
#     value = models.CharField(max_length=100, null=True, blank=True)
#     section_field = models.ForeignKey(SectionField, null=True, blank=True)
#     description = models.ForeignKey(Description, related_name='values', null=True, blank=True)
#     date_created = models.DateTimeField(blank=True, auto_now_add=True)
#     date_edited = models.DateTimeField(blank=True, auto_now=True)
