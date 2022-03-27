
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.page01,name="page01"),
    path('page02/', views.page02, name="page02")
]
