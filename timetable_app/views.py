from django.shortcuts import render, redirect, get_object_or_404
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.views import View
from xhtml2pdf import pisa
from datetime import datetime, timedelta
import random
from .models  import *
from .forms import *
from django.contrib import messages
from django.db.models import F, Q

# Create your views here.
def home(request):
    myTemplate = 'timetable/home.html'
    context = {}
    return render(request, myTemplate, context)

@login_required
def dashboard(request):
    sliced_venues = Venue.objects.all()[:5]
    sliced_modules = Module.objects.all()[:5]
    sliced_lecturers = Lecturer.objects.all()[:5]
    sliced_courses = Course.objects.all()[:5]
    venues_number = Venue.objects.all().count()
    modules_number = Module.objects.all().count()
    lecturers_number = Lecturer.objects.all().count()
    courses_number = Course.objects.all().count()

    myTemplate = 'timetable/dashboard.html'
    context = {
        'venues': sliced_venues,
        'modules': sliced_modules,
        'lecturers': sliced_lecturers,
        'courses': sliced_courses,
        'venues_number': venues_number,
        'modules_number': modules_number,
        'lecturers_number': lecturers_number,
        'courses_number': courses_number,
    }
    return render(request, myTemplate, context)

# ==================== Venue Logics ===========================================
@login_required
def view_venues(request):
    get_venues = Venue.objects.all()
    query = request.GET.get("q")
    if query:
        get_venues = get_venues.filter(name__icontains = query)
        if not get_venues:
            get_venues = Venue.objects.all()
            messages.warning(request,f'Invalid Search!')
    myTemplate = 'timetable/viewVenues.html'
    context = {
        'venues': get_venues,
    }
    return render(request, myTemplate, context)

@login_required
def add_venue(request):
    form   = addVenueForm()
    if request.method == 'POST':
        form = addVenueForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Venue added successfully!')
            return redirect('add-venue')
    else:
        add_form = addVenueForm()
    context = {
        'form': form,
    }
    myTemplate = 'timetable/addVenue.html'
    return render(request, myTemplate, context)

@login_required
def update_venue(request, id):
    instance = get_object_or_404(Venue, pk = id)
    form = updateVenueForm(request.POST or None, instance = instance)
    if form.is_valid():
        form.save()
        messages.success(request, f'Venue has been updated successifully!')
        return redirect ('view-venues')
    context = {
        'form': form,
    }
    myTemplate = 'timetable/updateVenue.html'
    return render(request, myTemplate, context)

@login_required
def delete_venue(request, id):
    get_data = get_object_or_404(Venue, pk = id)
    get_data.delete()
    messages.success(request, f'Venue deleted successfull!')
    return redirect('view-venues')


# ==================== Lecturers Logics ===========================================
@login_required
def view_lecturers(request):
    get_lecturers = Lecturer.objects.all()
    query = request.GET.get("q")
    if query:
        get_lecturers = get_lecturers.filter(Q(name__icontains = query) |Q(id_number__icontains = query) )
        if not get_lecturers:
            get_lecturers = Lecturer.objects.all()
            messages.warning(request,f'Invalid Search!')
    myTemplate = 'timetable/viewLecturers.html'
    context = {
        'lecturers': get_lecturers,
    }
    return render(request, myTemplate, context)

@login_required
def add_lecturer(request):
    form   = addLecturerForm()
    if request.method == 'POST':
        form = addLecturerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Lecturer added successfully!')
            return redirect('add-lecturer')
    else:
        add_form = addLecturerForm()
    context = {
        'form': form,
    }
    myTemplate = 'timetable/addLecturer.html'
    return render(request, myTemplate, context)

@login_required
def update_lecturer(request, id):
    instance = get_object_or_404(Lecturer, pk = id)
    form = updateLecturerForm(request.POST or None, instance = instance)
    if form.is_valid():
        form.save()
        messages.success(request, f'Lecturer has been updated successifully!')
        return redirect ('view-lecturers')
    context = {
        'form': form,
    }
    myTemplate = 'timetable/updateLecturer.html'
    return render(request, myTemplate, context)

@login_required
def delete_lecturer(request, id):
    get_data = get_object_or_404(Lecturer, pk = id)
    get_data.delete()
    messages.success(request, f'Lecturer deleted successfull!')
    return redirect('view-lecturers')

# ==================== Module Logics ===========================================
@login_required
def view_modules(request):
    get_modules = Module.objects.all()
    query = request.GET.get("q")
    if query:
        get_modules = get_modules.filter(Q(name__icontains = query) |Q(code__icontains = query) )
        if not get_modules:
            get_modules = Module.objects.all()
            messages.warning(request,f'Invalid Search!')
    myTemplate = 'timetable/viewModules.html'
    context = {
        'modules': get_modules,
    }
    return render(request, myTemplate, context)

@login_required
def add_module(request):
    form   = addModuleForm()
    if request.method == 'POST':
        form = addModuleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Module added successfully!')
            return redirect('add-module')
    else:
        add_form = addModuleForm()
    context = {
        'form': form,
    }
    myTemplate = 'timetable/addModule.html'
    return render(request, myTemplate, context)

@login_required
def update_module(request, id):
    instance = get_object_or_404(Module, pk = id)
    form = updateModuleForm(request.POST or None, instance = instance)
    if form.is_valid():
        form.save()
        messages.success(request, f'Module has been updated successifully!')
        return redirect ('view-modules')
    context = {
        'form': form,
    }
    myTemplate = 'timetable/updateModule.html'
    return render(request, myTemplate, context)

@login_required
def delete_module(request, id):
    get_data = get_object_or_404(Module, pk = id)
    get_data.delete()
    messages.success(request, f'Module deleted successfull!')
    return redirect('view-modules')

# ==================== Courses Logics ===========================================
@login_required
def view_courses(request):
    get_courses = Course.objects.all()
    query = request.GET.get("q")
    if query:
        get_courses = get_courses.filter(Q(name__icontains = query) |Q(code__icontains = query) )
        if not get_courses:
            get_courses = Course.objects.all()
            messages.warning(request,f'Invalid Search!')
    myTemplate = 'timetable/viewCourses.html'
    context = {
        'courses': get_courses,
    }
    return render(request, myTemplate, context)


def filterCourses(request):
    get_courses = Course.objects.all()
    query = request.GET.get("q")
    if query:
        get_courses = get_courses.filter(Q(name__icontains = query) |Q(code__icontains = query) )
        if not get_courses:
            get_courses = Course.objects.all()
            messages.warning(request,f'Invalid Search!')
    myTemplate = 'timetable/filterCourses.html'
    context = {
        'courses': get_courses,
    }
    return render(request, myTemplate, context)

@login_required
def add_course(request):
    form   = addCourseForm()
    if request.method == 'POST':
        form = addCourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Course added successfully!')
            return redirect('add-course')
    else:
        add_form = addCourseForm()
    context = {
        'form': form,
    }
    myTemplate = 'timetable/addCourse.html'
    return render(request, myTemplate, context)

@login_required
def update_course(request, id):
    instance = get_object_or_404(Course, pk = id)
    form = updateCourseForm(request.POST or None, instance = instance)
    if form.is_valid():
        form.save()
        messages.success(request, f'Course has been updated successifully!')
        return redirect ('view-courses')
    context = {
        'form': form,
    }
    myTemplate = 'timetable/updateCourse.html'
    return render(request, myTemplate, context)

@login_required
def delete_course(request, id):
    get_data = get_object_or_404(Course, pk = id)
    get_data.delete()
    messages.success(request, f'Course deleted successfull!')
    return redirect('view-courses')


#============================ Intervals ========================================
@login_required
def view_intervals(request):
    get_intervals = Interval.objects.all()
    query = request.GET.get("q")
    if query:
        get_intervals = get_intervals.filter(Q(start_time__icontains = query) |Q(end_time__icontains = query) )
        if not get_intervals:
            get_intervals = Interval.objects.all()
            messages.warning(request, f'Invalid Search!')
    myTemplate = 'timetable/viewIntervals.html'
    context = {
        'intervals': get_intervals,
    }
    return render(request, myTemplate, context)

@login_required
def add_interval(request):
    form   = addIntervalForm()
    if request.method == 'POST':
        form = addIntervalForm(request.POST)
        start_time = int(request.POST.get('start_time'))
        end_time = int(request.POST.get('end_time'))
        if form.is_valid():
            if start_time == end_time:
                messages.warning(request, f'Difference in two fields in mandatory!')
                return redirect('add-interval')
            elif start_time > 24 or end_time > 24:
                messages.warning(request, f'No field should exceed 24 hours!')
                return redirect('add-interval')
            else:
                    form.save()

                    messages.success(request, f'Time interval added successfully!')
                    return redirect('add-interval')
        else:
            messages.warning(request, f'Invalid form submitted!')
            return redirect('add-interval')
    else:
        add_form = addIntervalForm()
    context = {
        'form': form,
    }
    myTemplate = 'timetable/addInterval.html'
    return render(request, myTemplate, context)

@login_required
def update_interval(request, id):
    instance = get_object_or_404(Interval, pk = id)
    form = updateIntervalForm(request.POST or None, instance = instance)
    start_time = request.POST.get('start_time')
    end_time = request.POST.get('end_time')
    if form.is_valid():
        if start_time == end_time:
            messages.warning(request, f'Difference in two fields in mandatory!')
            return redirect('view-intervals')
        elif int(start_time) > 24 or int(end_time) > 24:
            messages.warning(request, f'No field should exceed 24 hours!')
            return redirect('view-intervals')
        else:
            form.save()
            messages.success(request, f'Time interval updated successfully!')
            return redirect('view-intervals')
    context = {
        'form': form,
    }
    myTemplate = 'timetable/updateInterval.html'
    return render(request, myTemplate, context)

@login_required
def delete_interval(request, id):
    get_data = get_object_or_404(Interval, pk = id)
    get_data.delete()
    messages.success(request, f'Interval deleted successfull!')
    return redirect('view-intervals')

#============================ Allocations ======================================
@login_required
def view_allocations(request):
    get_allocations = Allocation.objects.all()
    query = request.GET.get("q")
    if query:
        course = Course.objects.filter(Q(code__icontains = query) | Q(name__icontains = query))[:1]
        lecturer = Lecturer.objects.filter(Q(id_number__icontains = query) | Q(name__icontains = query))[:1]
        if course:
            get_allocations = get_allocations.filter(course = course)
        elif lecturer:
            get_allocations = get_allocations.filter(lecturer = lecturer)
        else:
            messages.warning(request, f'Invalid Search!!')
    myTemplate = 'timetable/viewAllocations.html'
    context = {
        'allocations': get_allocations,
    }
    return render(request, myTemplate, context)

@login_required
def add_allocation(request):
    form = addAllocationForm()
    if request.method == 'POST':
        form = form = addAllocationForm(request.POST)
        if form.is_valid():

            # time format
            tFormat = '%H'
            # Time interval for lessons
            get_interval = int(request.POST.get('interval'))

            get_day = request.POST.get('day')
            get_course = request.POST.get('course')
            get_lecturer = request.POST.get('lecturer')
            get_module = request.POST.get('module')

            course = Course.objects.get(id = get_course)
            lecturer = Lecturer.objects.get(id = get_lecturer)
            module = Module.objects.get(id = get_module)
            interval = Interval.objects.get(id = get_interval)
            day = Day.objects.get(id = get_day)


            # get the selected interval from db
            interval = Interval.objects.filter(id = get_interval)[0]


            get_type = int(request.POST.get('type'))

            print(get_type)

            # Convert string data from user to time format
            start_time = datetime.strptime(str(interval.start_time), tFormat)
            end_time = datetime.strptime(str(interval.end_time), tFormat)

            # get difference between two times
            difference = end_time - start_time

            # convert to hours
            hrs = difference.seconds//3600

            # find random time between the difference of the interval
            random_hours = random.randint(0,hrs)

            # start lesson time without end class time
            start_lesson = start_time + timedelta(hours = random_hours)

            # calculate with end of the lecture
            end_lesson = start_lesson + timedelta(hours = get_type)

            allocated = start_lesson.strftime('%H:%M') + ' - ' + end_lesson.strftime('%H:%M')
            print('The lecture  will be on ', allocated)


            # Getting random venues from db
            get_venues = Venue.objects.all()
            # Create empty list to store selected venues
            venues = []

            # From course selected by user
            course = Course.objects.filter(id = get_course)[0]

            # Loop through each venue and check venue capacity
            for get_venue in get_venues:
                if get_venue.capacity >= course.capacity:
                    venues.append(get_venue)
            if venues:
                random_venue = random.choice(venues)
            else:
                messages.warning(request, f'There is no venue to accomodate this course\'s capacity!!')
                return redirect('add-allocation')

            # Starting allocating venues and time
            allocations = Allocation.objects.all()

            if allocations:

                # Count number of lessons of the lecturer per day
                allocation = allocations.filter(day = day, lecturer = lecturer).count()
                # If any return a message
                if allocation > 3:
                    messages.warning(request, f'This lecturer has already satisfied day\'s lessons!!')
                    return redirect('add-allocation')

                # Check for repeated allocations
                allocation = allocations.filter(day = day, course = course, module = module, type = get_type )
                # If anf return message
                if allocation:
                    messages.warning(request, f'This allocation already exists!! You can change type if you understand why')
                    return redirect('add-allocation')

                # Check collitions for lecturer's time
                if allocations.filter(day = day, lecturer = lecturer, start_lesson__range = [ start_lesson, end_lesson]) or allocations.filter(day = day, lecturer = lecturer, end_lesson__range = [ start_lesson, end_lesson]):
                    count = 0

                    start_time_allocation = allocations.filter(day = day, lecturer = lecturer, start_lesson__range = [ start_lesson, end_lesson])

                    end_time_allocation = allocations.filter(day = day, lecturer = lecturer, end_lesson__range = [ start_lesson, end_lesson])

                    while start_time_allocation or end_time_allocation:

                        # find random time between the difference of the interval
                        random_hours = random.randint(0,hrs)

                        # start lesson time without end class time
                        start_lesson = start_time + timedelta(hours = random_hours)

                        # calculate with end of the lecture
                        end_lesson = start_lesson + timedelta(hours = get_type)

                        count += 1

                        if count >= hrs:
                            messages.warning(request, f'This lecturer looks like occupied for this day!! Resubmit form again or you can choose another day!!')
                            return redirect('add-allocation')

                # Check collitions for Venue's time
                if allocations.filter(day = day, venue = venue, start_lesson__range = [ start_lesson, end_lesson]) or allocations.filter(day = day, venue = venue, end_lesson__range = [ start_lesson, end_lesson]):

                    start_time_allocation = allocations.filter(day = day, venue = venue, start_lesson__range = [ start_lesson, end_lesson])

                    end_time_allocation = allocations.filter(day = day, venue = venue, end_lesson__range = [ start_lesson, end_lesson])

                    count = 0
                    while start_time_allocation or end_time_allocation:

                        # Run random choice of venues again
                        random_venue = random.choice(venues)

                        # find random time between the difference of the interval
                        random_hours = random.randint(0,hrs)

                        # start lesson time without end class time
                        start_lesson = start_time + timedelta(hours = random_hours)

                        # calculate with end of the lecture
                        end_lesson = start_lesson + timedelta(hours = get_type)

                        count += 1

                        if count >= hrs:
                            messages.warning(request, f'Can\'t find time and venue!! Resubmit form again or you can choose another day!!')
                            return redirect('add-allocation')


                form = Allocation (
                    day = day,
                    course= course,
                    lecturer = lecturer,
                    start_lesson =  start_lesson,
                    end_lesson = end_lesson,
                    venue = random_venue,
                    type = get_type,
                    interval = interval,
                    module = module,
                )
                form.save()
                messages.success(request, f'Allocation added successfully!')
                return redirect('add-allocation')
            else:
                form = Allocation (
                    day = day,
                    course= course,
                    lecturer = lecturer,
                    start_lesson =  start_lesson,
                    end_lesson = end_lesson,
                    venue = random_venue,
                    type = get_type,
                    interval = interval,
                    module = module,
                )
                form.save()
                messages.success(request, f'Allocation added successfully!')
                return redirect('add-allocation')
    myTemplate = 'timetable/addAllocation.html'
    context = {
        'form': form,
    }
    return render(request, myTemplate, context)


@login_required
def update_allocation(request, id):
    instance = get_object_or_404(Allocation, pk = id)
    form = updateAllocationForm(request.POST or None, instance = instance)

    if form.is_valid():
        form.save()
        messages.success(request, f'Allocation updated successfully!')
        return redirect('view-allocations')
    context = {
        'form': form,
    }
    myTemplate = 'timetable/updateAllocation.html'
    return render(request, myTemplate, context)


def delete_allocation(request, id):
    get_data = get_object_or_404(Allocation, pk = id)
    get_data.delete()
    messages.success(request, f'Allocation deleted successfull!')
    return redirect('view-allocations')



# ===================================== PDF ====================================
def pdf(request, id):
    course = Course.objects.get(id = id)
    days = Day.objects.filter()[:5]
    allocations = Allocation.objects.filter(course = course).order_by('start_lesson')
    count = 0
    if allocations:
        for day in days:
            if allocations.filter(day = day):
                continue
            else:
                count += 1
                continue
    if allocations:
        context = {
            'course': course,
            'days': days,
            'allocations': allocations,
            'count': count,
        }
        myTemplate = 'timetable/pdf.html'
        return render(request, myTemplate, context)
    else:
        messages.warning(request, f'No timetable, create allocations first!!')
        return redirect('view-allocations')

def render_to_pdf(template_src, context = {}):
    template = get_template(template_src)
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type = 'application/pdf')
    return None

class ViewPDF(View):
    def get(self, request, id, *args, **kwargs):
        course = Course.objects.get(id = id)
        days = Day.objects.filter()[:5]
        allocations = Allocation.objects.filter(course = course).order_by('start_lesson')
        if allocations:
            context = {
                'course': course,
                'days': days,
                'allocations': allocations,
            }
            myTemplate = 'timetable/pdfdownloadable.html'
            pdf = render_to_pdf(myTemplate, context)
            if pdf:
                return HttpResponse(pdf, content_type = 'application/pdf')
            else:
                return HttpResponse('Not found')
        else:
            messages.warning(request, f'No timetable, create allocations first!!')
            return redirect('view-allocations')


class DownloadPDF(View):
    def get(self, request, id, *args, **kwargs):
        course = Course.objects.get(id = id)
        days = Day.objects.filter()[:5]
        allocations = Allocation.objects.filter(course = course).order_by('start_lesson')
        if allocations:
            context = {
                'course': course,
                'days': days,
                'allocations': allocations,
            }
            myTemplate = 'timetable/pdfdownloadable.html'
            pdf = render_to_pdf(myTemplate, context)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = f'Timetable_{ course.code }.pdf'
                content = f"attachment; filename = {filename} "
                response['Content-Disposition'] = content
                if response:
                    return response
                else:
                    return HttpResponse('Not found')
        else:
            messages.warning(request, f'No timetable, create allocations first!!')
            return redirect('view-allocations')
