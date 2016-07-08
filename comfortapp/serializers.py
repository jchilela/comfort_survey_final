from rest_framework import serializers
from .models import task

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = task
		fields = ('id', 'task_name', 'task_desc')