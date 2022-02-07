from django.urls import path
from .views import *

urlpatterns = [
    path('courses/', CoursesList.as_view()),
    # path('create-course/', CourseCreate.as_view()),
    # path('update-course/<int:pk>/', CourseRetrieveUpdateDestroy.as_view()),
    # path('course/<int:pk>/complete', CourseComplete.as_view()),
    path('course/<int:pk>/', CourseDetailView, name = 'course'),
    path('create-course/', CourseCreateView, name = 'course-create'),
    path('update-course/<int:pk>/', CourseUpdateView, name = 'course-update'),
    path('delete-course/<int:pk>/', CourseDeleteView, name = 'course-delete'),

    # Authentication
    path('signup/', signup),
    path('login/', login),
]
