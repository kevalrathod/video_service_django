
from django.urls import path
from .views import CourseListView, CourseDetailView

app_name='courses'

urlpatterns = [
    path('' , CourseListView.as_view(),name='list'),
    path('<slig>' ,CourseDetailView.as_view(),name='detail'),
]

