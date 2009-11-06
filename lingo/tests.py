from django.contrib.auth.models import User
from django.db import models
from django.test import TestCase

from lingo.forms import LingoForm
from lingo.models import LabelCustomization

class TestModel(models.Model):
    name = models.CharField(max_length=200)
    rank = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=200)

class LingoTestCase(TestCase):
    def setUp(self):
        self.user = User()
        self.user.username = 'tester'
        self.user.email = 'tester@tester.com'
        self.user.save()
        lc = LabelCustomization()
        lc.user = self.user
        lc.app_label = 'lingo'
        lc.model_name = 'testmodel'
        lc.field = 'rank'
        lc.custom_label = 'Job Level'
        lc.save()
    
    def test_customization(self):
        class TestForm(LingoForm):
            
            class Meta:
                model = TestModel
        
        uncustomized_form = TestForm()
        self.assertEquals(uncustomized_form.fields['rank'].label, 'Rank')
        customized_form = TestForm(user=self.user)
        self.assertEquals(customized_form.fields['rank'].label, 'Job Level')
        

