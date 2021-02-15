from django.urls import path, include

from .views import add_job, job_details, apply_for_job

urlpatterns = [
    path('add/', add_job, name='add_job'),
    path('<int:job_id>', job_details, name='job_details'),
    path('<int:job_id>/apply_for_job/', apply_for_job, name='apply_for_job')

]
