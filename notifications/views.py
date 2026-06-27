from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Notification


@login_required
def notifications_list(request):
    notifications = Notification.objects.filter(recipient=request.user)
    unread_count = notifications.filter(is_read=False).count()

    # Mark all as read when viewed
    notifications.filter(is_read=False).update(is_read=True)

    return render(request, 'notifications/list.html', {
        'notifications': notifications,
        'unread_count': unread_count,
    })


@login_required
def mark_read(request, pk):
    notif = get_object_or_404(Notification, pk=pk, recipient=request.user)
    notif.is_read = True
    notif.save()
    return redirect('notifications:list')


@login_required
def clear_all(request):
    if request.method == 'POST':
        Notification.objects.filter(recipient=request.user).delete()
    return redirect('notifications:list')