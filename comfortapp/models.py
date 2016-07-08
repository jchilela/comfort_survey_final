from django.db import models

# Create your models here.
class index(models.Model):
	preference = models.CharField(max_length=50)
	def __unicode__(self):
		return unicode(self.preference)

class task(models.Model):

	task_name = models.CharField(max_length=100)
	task_desc = models.CharField(max_length=100)
	data_created = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return "%s" % self.task_name
