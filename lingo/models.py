from django.contrib.auth.models import User
from django.db import models

class LabelCustomization(models.Model):
    """Label customization object to translate model field labels into different business lingo"""
    user = models.ForeignKey(User)
    app_label = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    field = models.CharField(max_length=100)
    custom_label = models.CharField(max_length=200)
    
    def __unicode__(self):
        return "Label Customization"
