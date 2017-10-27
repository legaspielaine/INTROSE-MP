from django.conf.urls import url
from . import views

app_name = 'acctsys'

urlpatterns = [ 
    url(r'^$', views.index, name='index'),
    url(r'^branch/$', views.branch, name='branch'),
    url(r'^coa/$', views.coa, name='coa'),
    url(r'^inventory/$', views.inventory, name='inventory'),
    url(r'^addBranch/$', views.addBranch, name='addBranch'),
    url(r'^addCOA/$', views.addCOA, name='addCOA'),
    url(r'^addProduct/$', views.addProduct, name='addProduct'),

]