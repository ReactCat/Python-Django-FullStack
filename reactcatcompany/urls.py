from django.contrib import admin
from django.urls import path
from reactcatcompany import views


urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('companyinfo', views.companyinfo, name="companyinfo"),
    path('pythonintro', views.pythonintro, name="pythonintro"),
    path('pythonadvanced', views.pythonadvanced, name="pythonadvanced"),
    path('pythonpandas', views.pythonpandas, name="pythonpandas"),
    path('pythondjango', views.pythondjango, name="pythondjango"),
    path('pydjangoecom', views.pydjangoecom, name="pydjangoecom"),
    path('pydjangoapi', views.pydjangoapi, name="pydjangoapi"),
    path('pythonreact', views.pythonreact, name="pythonreact"),
    path('pybusinessit', views.pybusinessit, name="pybusinessit"),

    path('jpn/homejpn', views.homejpn, name="homejpn"),
    path('jpn/contactjpn', views.contactjpn, name="contactjpn"),
    path('jpn/companyinfojpn', views.companyinfojpn, name="companyinfojpn"),
    path('jpn/pythonintrojpn', views.pythonintrojpn, name="pythonintrojpn"),
    path('jpn/pythonadvancedjpn', views.pythonadvancedjpn, name="pythonadvancedjpn"),
    path('jpn/pythonpandasjpn', views.pythonpandasjpn, name="pythonpandasjpn"),
    path('jpn/pythondjangojpn', views.pythondjangojpn, name="pythondjangojpn"),
    path('jpn/pydjangoecomjpn', views.pydjangoecomjpn, name="pydjangoecomjpn"),
    path('jpn/pydjangoapijpn', views.pydjangoapijpn, name="pydjangoapijpn"),
    path('jpn/pythonreactjpn', views.pythonreactjpn, name="pythonreactjpn"),
    path('jpn/pybusinessitjpn', views.pybusinessitjpn, name="pybusinessitjpn"),
    

]

