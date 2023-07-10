from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('ToDoListComponent/', include('ToDoListComponent.urls')),
    path('admin/', admin.site.urls),
]