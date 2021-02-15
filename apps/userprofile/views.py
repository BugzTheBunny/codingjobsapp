from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from apps.job.models import Application, Job
from apps.userprofile.models import ConversationMessage
from apps.notification.utilities import create_notification


@login_required
def dashboard(request):
    context = {
        'userprofile': request.user.userprofile
    }
    return render(request, 'userprofile/dashboard.html', context)


@login_required
def view_dashboard_job(requset, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=requset.user)
    context = {
        'job': job
    }

    return render(requset, 'userprofile/view_dashboard_job.html', context)


@login_required
def view_application(request, application_id):
    if request.user.userprofile.is_employer:
        application = get_object_or_404(Application, pk=application_id, job__created_by=request.user)
    else:
        application = get_object_or_404(Application, pk=application_id, created_by=request.user)

    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            conversationmessage = ConversationMessage.objects.create(application=application, content=content,
                                                                     created_by=request.user)

            create_notification(request, to_user=application.created_by, notification_type="message",
                                extra_id=application.id)
            return redirect('view_application', application_id)
    context = {
        'application': application
    }
    return render(request, 'userprofile/view_application.html', context)
