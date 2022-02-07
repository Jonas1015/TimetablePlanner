from django import forms
from .models import *

# Create your forms here
class addVenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'capacity']

class addLecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ['id_number', 'name', 'speciality']

class addModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['code', 'name', 'course']

class addCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name', 'capacity']

# ========================UPDATE ================================================
class updateVenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'capacity']

class updateLecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ['id_number', 'name', 'speciality']

class updateModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['code', 'name', 'course']

class updateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name', 'capacity']

#========================== Intervals =========================================
class addIntervalForm(forms.ModelForm):
    class Meta:
        model = Interval
        fields = ['start_time', 'end_time']

        widget = {
            'start_time' : forms.TextInput(attrs = {'type': 'number', 'max': '24' }),
            'end_time' : forms.TextInput(attrs = { 'type': 'number', 'max': '24'})
        }

class updateIntervalForm(forms.ModelForm):
    class Meta:
        model = Interval
        fields = ['start_time', 'end_time']

#========================== ALLOCATIONS =========================================
class addAllocationForm(forms.ModelForm):
    class Meta:
        model = Allocation
        fields = ['day', 'course', 'module', 'lecturer', 'type', 'interval']


class updateAllocationForm(forms.ModelForm):
    class Meta:
        model = Allocation
        fields = ['day', 'course', 'module', 'lecturer','venue', 'type', 'interval', 'start_lesson', 'end_lesson']
