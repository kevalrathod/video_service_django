from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Courses
# Create your views here.


class CourseListView(ListView):
	model=Courses

class CourseDetailView(DetailView):
	model=Courses