from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import PythonCourse
from .models import PythonCourseJPN


""" English Site Templates """

def home(request):
    return render(request, 'reactcatcompany/home.html')

def companyinfo(request):
    return render(request, 'reactcatcompany/companyinfo.html')

def contact(request):
    if request.method == "POST":
        sender_name = request.POST['sender-name']
        sender_email = request.POST['sender-email']
        sender_message = request.POST['sender-message']

        #Send Email
        send_mail(sender_name, sender_message,sender_email,
         ['reactcatkris@gmail.com'], )

        return render(request, 'reactcatcompany/contact.html',
        {'sender_name': sender_name})
    else:
        return render(request, 'reactcatcompany/contact.html')


def pythonintro(request):
    pythoncourse = PythonCourse.objects.all().order_by('coursename')

    return render(request, 'reactcatcompany/pythonintro.html',
     {'pythoncourse': pythoncourse,} )


def pythonadvanced(request):
    pythoncourse = PythonCourse.objects.all().order_by('coursename')

    return render(request, 'reactcatcompany/pythonadvanced.html',
     {'pythoncourse': pythoncourse,} )

def pythonpandas(request):
    pythoncourse = PythonCourse.objects.all().order_by('coursename')

    return render(request, 'reactcatcompany/pythonpandas.html',
     {'pythoncourse': pythoncourse,} )

def pythondjango(request):
    pythoncourse = PythonCourse.objects.all().order_by('coursename')

    return render(request, 'reactcatcompany/pythondjango.html',
     {'pythoncourse': pythoncourse,} )

def pydjangoecom(request):
    pythoncourse = PythonCourse.objects.all().order_by('coursename')

    return render(request, 'reactcatcompany/pydjangoecom.html',
     {'pythoncourse': pythoncourse,} )

def pydjangoapi(request):
    pythoncourse = PythonCourse.objects.all().order_by('coursename')

    return render(request, 'reactcatcompany/pydjangoapi.html',
     {'pythoncourse': pythoncourse,} )


def pythonreact(request):
    pythoncourse = PythonCourse.objects.all().order_by('coursename')

    return render(request, 'reactcatcompany/pythonreact.html',
     {'pythoncourse': pythoncourse,} )

def pybusinessit(request):
    pythoncourse = PythonCourse.objects.all().order_by('coursename')

    return render(request, 'reactcatcompany/pybusinessit.html',
     {'pythoncourse': pythoncourse,} )





""" Japanese Site Templates """

def homejpn(request):
    return render(request, 'reactcatcompany/jpn/homejpn.html')

def companyinfojpn(request):
    return render(request, 'reactcatcompany/jpn/companyinfojpn.html')

def contactjpn(request):
    if request.method == "POST":
        sender_name = request.POST['sender-name']
        sender_email = request.POST['sender-email']
        sender_message = request.POST['sender-message']

        #Send Email
        send_mail(sender_name, sender_message,sender_email,
         ['reactcatkris@gmail.com'], )

        return render(request, 'reactcatcompany/jpn/contactjpn.html',
        {'sender_name': sender_name})
    else:
        return render(request, 'reactcatcompany/jpn/contactjpn.html')


def pythonintrojpn(request):
    pythoncourse = PythonCourseJPN.objects.all().order_by('coursename')

    return render(request, 'reactcatcompany/jpn/pythonintrojpn.html',
     {'pythoncourse': pythoncourse,} )


def pythonadvancedjpn(request):
    pythoncourse = PythonCourseJPN.objects.all().order_by('coursename')

    return render(request, 'reactcatcompany/jpn/pythonadvancedjpn.html',
     {'pythoncourse': pythoncourse,} )

def pythonpandasjpn(request):
    pythoncourse = PythonCourseJPN.objects.all().order_by('coursename')

    return render(request, 'reactcatcompany/jpn/pythonpandasjpn.html',
     {'pythoncourse': pythoncourse,} )

def pythondjangojpn(request):
    pythoncourse = PythonCourseJPN.objects.all().order_by('coursename')

    return render(request, 'reactcatcompany/jpn/pythondjangojpn.html',
     {'pythoncourse': pythoncourse,} )

def pydjangoecomjpn(request):
    pythoncourse = PythonCourseJPN.objects.all().order_by('coursename')

    return render(request, 'reactcatcompany/jpn/pydjangoecomjpn.html',
     {'pythoncourse': pythoncourse,} )

def pydjangoapijpn(request):
    pythoncourse = PythonCourseJPN.objects.all().order_by('coursename')

    return render(request, 'reactcatcompany/jpn/pydjangoapijpn.html',
     {'pythoncourse': pythoncourse,} )


def pythonreactjpn(request):
    pythoncourse = PythonCourseJPN.objects.all().order_by('coursename')

    return render(request, 'reactcatcompany/jpn/pythonreactjpn.html',
     {'pythoncourse': pythoncourse,} )

def pybusinessitjpn(request):
    pythoncourse = PythonCourseJPN.objects.all().order_by('coursename')

    return render(request, 'reactcatcompany/jpn/pybusinessitjpn.html',
     {'pythoncourse': pythoncourse,} )

