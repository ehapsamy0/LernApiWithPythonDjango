from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('courses',views.CourseView)

app_name = 'courses'

urlpatterns = [
	path('',include(router.urls)),

]
