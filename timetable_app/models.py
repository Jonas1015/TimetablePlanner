from django.db import models

# Create your models here.
class Day(models.Model):
    name = models.CharField(max_length = 20, unique = True)



    class Meta:
        verbose_name_plural = 'Days'

    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length = 20, unique = True)
    capacity = models.PositiveIntegerField(default = 0)


    class Meta:
        verbose_name_plural = 'Venues'

    def __str__(self):
        return self.name


class Lecturer(models.Model):
    id_number = models.CharField(max_length = 50, unique = True)
    name = models.CharField(max_length = 100)
    speciality = models.CharField(max_length = 100)


    class Meta:
        verbose_name_plural = 'Lecturers'

    def __str__(self):
        return self.name


class Course(models.Model):
    code = models.CharField(max_length = 20, unique = True)
    name = models.CharField(max_length = 100)
    capacity = models.PositiveIntegerField(default = 0)

    class Meta:
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name + ' ' +  '(' + self.code + ')'

class Module(models.Model):
    code = models.CharField(max_length = 20, unique = True)
    name = models.CharField(max_length = 100)
    course = models.ForeignKey(Course, models.SET_NULL, blank = True, null = True)

    class Meta:
        verbose_name_plural = 'Modules'

    def __str__(self):
        return self.name + ' '+ '(' + self.code + ')'

class Interval(models.Model):
    start_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Intervals'

    def __str__(self):
        start_time = str(self.start_time)
        end_time = str(self.end_time)
        return start_time +" - "+ end_time


TYPE_CHOICES = (
    ('1', 'Tutorial / Seminar'),
    ('2', 'Lecture'),
)

class Allocation(models.Model):
    day = models.ForeignKey(Day, models.SET_NULL, blank = True, null = True)
    course  = models.ForeignKey(Course, on_delete = models.CASCADE)
    lecturer  = models.ForeignKey(Lecturer, on_delete = models.CASCADE)
    start_lesson = models.TimeField()
    end_lesson = models.TimeField()
    venue  = models.ForeignKey(Venue, on_delete = models.CASCADE)
    type = models.CharField(choices = TYPE_CHOICES, max_length = 2)
    interval = models.ForeignKey(Interval, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'Allocations'

    def __str__(self):
        return self.day + self.time
