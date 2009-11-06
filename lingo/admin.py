from django.contrib import admin
from lingo.models import LabelCustomization

class LabelCustomizationAdmin(admin.ModelAdmin):
    list_display = ['user', 'app_label', 'model_name', 'field', 'custom_label']
    raw_id_fields = ['user']

admin.site.register(LabelCustomization, LabelCustomizationAdmin)
