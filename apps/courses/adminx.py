import xadmin

from apps.courses.models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'desc', 'degree', 'learn_times', 'students']
    search_fields = ['name', 'desc', 'degree',  'students']
    list_filter = ['name', 'desc', 'degree', 'learn_times', 'students']
    list_editable = ['degree', 'desc']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['couese', 'name']
    list_filter = ['course_name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'add_time', 'download']

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)