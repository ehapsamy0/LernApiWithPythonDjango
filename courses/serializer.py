from rest_framework import serializers
from .models import Courses

class CourseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Courses
		fields = ('id','name','language','price')