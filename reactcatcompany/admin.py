from django.contrib import admin


from .models import PythonCourse
from .models import PythonCourseJPN


admin.site.register(PythonCourse)
admin.site.register(PythonCourseJPN)

