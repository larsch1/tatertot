
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
