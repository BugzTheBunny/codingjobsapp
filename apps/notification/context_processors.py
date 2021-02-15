from .models import Notification


def notifications(request):
    if request.user.is_authenticated:
        notifications = request.user.notifications.filter(is_read=False)
        context = {
            'notifications': notifications
        }
        return context
    else:
        context = {
            'notifications': []
        }
        return context
