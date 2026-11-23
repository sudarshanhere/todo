from django.http import FileResponse
from django.urls import path
from .views import home,update,delete

urlpatterns=[
    path('', home, name='home'),
    path('LLms.txt', lambda request: FileResponse(open('LLms.txt', 'rb'), content_type='text/plain')),
    path('Robot.txt', lambda request: FileResponse(open('Robot.txt', 'rb'), content_type='text/plain')),
    path('update/<int:task_id>/', update, name='update'),
    path('delete/<int:task_id>/', delete, name='delete'),
]