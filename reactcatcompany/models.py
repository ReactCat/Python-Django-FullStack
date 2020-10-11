from django.db import models


class PythonCourse(models.Model):
    coursecode = models.IntegerField()
    coursename = models.CharField(max_length=255)
    courseovertit = models.CharField(max_length=255, null=True)
    courseoverdet = models.TextField(blank=True)
    coursereqtit = models.CharField(max_length=255, null=True)
    coursereqdet = models.TextField(blank=True)
    coursecover = models.CharField(max_length=255, blank=True)
    courseinfo1 = models.TextField(blank=True)
    courseinfo2 = models.TextField(blank=True)
    courseinfo3 = models.TextField(blank=True)
    courseinfo4 = models.TextField(blank=True)
    courseinfo5 = models.TextField(blank=True)
    courseinfo6 = models.TextField(blank=True)
    courseinfo7 = models.TextField(blank=True)
    courseinfo8 = models.TextField(blank=True)
    courseinfo9 = models.TextField(blank=True)
    courseinfo10 = models.TextField(blank=True)
    courseinfo11= models.TextField(blank=True)
    courseinfo12 = models.TextField(blank=True)
    courseinfo13 = models.TextField(blank=True)
    courseinfo14 = models.TextField(blank=True)  
    coursestart = models.CharField(max_length=255, null=True)
    contactdetails = models.TextField(max_length=255, null=True)
    
    


    def __str__(self):
        return str(self.coursecode)

    class Meta:
       
       verbose_name_plural = "Python Course"


class PythonCourseJPN(models.Model):
    coursecode = models.IntegerField()
    coursename = models.CharField(max_length=255)
    courseovertit = models.CharField(max_length=255, null=True)
    courseoverdet = models.TextField(blank=True)
    coursereqtit = models.CharField(max_length=255, null=True)
    coursereqdet = models.TextField(blank=True)
    coursecover = models.CharField(max_length=255, blank=True)
    courseinfo1 = models.TextField(blank=True)
    courseinfo2 = models.TextField(blank=True)
    courseinfo3 = models.TextField(blank=True)
    courseinfo4 = models.TextField(blank=True)
    courseinfo5 = models.TextField(blank=True)
    courseinfo6 = models.TextField(blank=True)
    courseinfo7 = models.TextField(blank=True)
    courseinfo8 = models.TextField(blank=True)
    courseinfo9 = models.TextField(blank=True)
    courseinfo10 = models.TextField(blank=True)
    courseinfo11= models.TextField(blank=True)
    courseinfo12 = models.TextField(blank=True)
    courseinfo13 = models.TextField(blank=True)
    courseinfo14 = models.TextField(blank=True)  
    coursestart = models.CharField(max_length=255, null=True)
    contactdetails = models.TextField(max_length=255, null=True)
    
    


    def __str__(self):
        return str(self.coursecode)

    class Meta:
       
       verbose_name_plural = "Python Course JPN"


    
