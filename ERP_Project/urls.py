
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('questions/', include('questions.urls')),
# ]

# from django.conf.urls import url, include
# from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^questions/', include('questions.urls')),
# ]


from django.conf.urls import url
from django.contrib import admin

from questions import views

urlpatterns = [
    url(r'^$', views.home, name='home'), # home page
    url(r'^admin/', admin.site.urls), # admin page
    url(r'^questions/', views.questions, name='questions'), # questions page
    url(r'^candidates/', views.candidates, name='candidates'), # candidate page
]