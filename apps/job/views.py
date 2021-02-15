from django.shortcuts import render, redirect
from .models import Job
from .forms import AddJobForm, ApplicationForm
from apps.notification.utilities import create_notification

from django.contrib.auth.decorators import login_required


def job_details(request, job_id):
    job = Job.objects.get(pk=job_id)
    context = {
        'job': job
    }
    return render(request, 'job/job_details.html', context)


@login_required
def apply_for_job(request, job_id):
    job = Job.objects.get(pk=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.save()

            create_notification(request, to_user=job.created_by, notification_type="application",
                                extra_id=application.id)

            return redirect('dashboard')
    else:
        form = ApplicationForm()

    context = {
        'form': form,
        'job': job
    }

    return render(request, 'job/apply_for_job.html', context)


@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            return redirect('dashboard')
    else:
        form = AddJobForm()
    context = {
        'form': form
    }
    return render(request, 'job/add_job.html', context)
