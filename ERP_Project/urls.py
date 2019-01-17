from django.conf.urls import url
from django.contrib import admin

from questions import views

urlpatterns = [
    url(r'^$', views.home, name='home'), # home page
    url(r'^admin/', admin.site.urls), # admin page
    url(r'^candidates/', views.candidates, name='candidates'), # candidate page
    url(r'^data/', views.data, name='data_analysis'), # data page
    url(r'^questions/', views.questions, name='questions'), # questions page
    url(r'^report/', views.report, name='report'), # report page
    url(r'^login/$', views.login_view, name='login'), # login page
    url(r'^logout/$', views.logout_view, name='logout') # logout page
]