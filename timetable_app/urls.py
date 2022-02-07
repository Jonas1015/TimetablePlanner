from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home' ),
    path('dashboard/', dashboard, name = 'dashboard' ),

    # ============================Venue ===================================
    path('all-venues/', view_venues, name = 'view-venues'),
    path('add/venue/', add_venue, name = 'add-venue'),
    path('update/venue/<int:id>/', update_venue, name = 'update-venue'),
    path('delete/venue/<int:id>/', delete_venue, name = 'delete-venue'),

    # ============================Lecturers ===================================
    path('all-lecturers/', view_lecturers, name = 'view-lecturers'),
    path('add/lecturer/', add_lecturer, name = 'add-lecturer'),
    path('update/lecturer/<int:id>/', update_lecturer, name = 'update-lecturer'),
    path('delete/lecturer/<int:id>/', delete_lecturer, name = 'delete-lecturer'),

    # ============================Modules ===================================
    path('all-modules/', view_modules, name = 'view-modules'),
    path('add/module/', add_module, name = 'add-module'),
    path('update/module/<int:id>/', update_module, name = 'update-module'),
    path('delete/module/<int:id>/', delete_module, name = 'delete-module'),

    # ============================Courses ===================================
    path('all-courses/', view_courses, name = 'view-courses'),
    path('add/course/', add_course, name = 'add-course'),
    path('update/course/<int:id>/', update_course, name = 'update-course'),
    path('delete/course/<int:id>/', delete_course, name = 'delete-course'),

    # ============================Allocations ===================================
    path('all-intervals/', view_intervals, name = 'view-intervals'),
    path('add/interval/', add_interval, name = 'add-interval'),
    path('update/interval/<int:id>/', update_interval, name = 'update-interval'),
    path('delete/course/<int:id>/', delete_interval, name = 'delete-interval'),

    # ============================Allocations ===================================
    path('all-allocations/', view_allocations, name = 'view-allocations'),
    path('add/allocation/', add_allocation, name = 'add-allocation'),
    path('update/allocation/<int:id>/', update_allocation, name = 'update-allocation'),
    path('delete/allocation/<int:id>/', delete_allocation, name = 'delete-allocation'),

    # ============================Allocations ===================================
    path('filter-by/courses/', filterCourses, name  ='filter-courses'),
    path('allocations/pdf/<int:id>/', pdf, name = 'pdf'),
    path('view/pdf/<int:id>/', ViewPDF.as_view(), name = 'viewPdf'),
    path('download/pdf/<int:id>/', DownloadPDF.as_view(), name = 'downloadPdf'),

]
